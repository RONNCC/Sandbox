   package IDT;

 /*
 * A code sprint by a person in 2 hours to try and track window movement / desktop movement
 * given a number of conditions and constant image values.
 */

  
   import java.io.File;
   import java.lang.Exception;
   import java.lang.String;
   import java.util.ArrayList;
   import java.awt.image.BufferedImage;
   import javax.imageio.ImageIO;
   import java.util.concurrent.*;
   import IDT.ImageOperations.CannyEdgeDetector;
   import IDT.ImageOperations.ImageOps;
	
   class IDT{
   //where are the images located
      public static String image_sub_dir = "IDT\\Images\\";
      //what I append to my  intermediary out files used for debugging / output
      public static String out_ext = "outf";
      public static void main(String[] args) throws Exception
      {
      /*
      * read in image
      */
         File[] images = readin();
      
      /*
      * process it
      */
         ImagePair[] pairs = process(images);
         
      /*
      * classify it
      */
         classify(pairs);
      }
     
   //helper method for conciseness
      public static void print(String a)
      {System.out.println(a);}
      public static <T> void printobj(T a)
      {System.out.println(a);}
      public static File[] remove_dirs_and_other_types(File[] f)
      {
      //removes directories from a list of paths
         ArrayList<File> file_ar = new ArrayList<File>();
         for(File fi: f){
            if(fi.isFile() && fi.getPath().indexOf(out_ext)!=-1){ 
               file_ar.add(fi);
            }
         }
         return file_ar.toArray(new File[]{});
      }
      
      /*
   	* Method that reads in the files. 
   	*/
      public static File[] readin(){
         File dir = new File(image_sub_dir);
         File[] image_names = null; //essentially only declare it.
         try{
            if(!dir.isDirectory()){
               throw new IsNotDirectoryException();
            }
            else{
               image_names = remove_dirs_and_other_types(dir.listFiles());
            }
         }
            catch(Exception e)
            {
               print("Image Directory was expected but not received");
               print("Received "+ dir.getAbsolutePath());
               System.exit(1);
            }
         File[] imagenames = dir.listFiles();
         assert image_names != null : "The image names dir could not be read";
         return imagenames;
      }
   	/*
   	* Method that processes the images and classifies the changes
   	*/
      public static ImagePair[] process(File[] imgs) throws Exception
      {
      
         ParsedImage[] parsed = new ParsedImage[imgs.length];
         for(int i=0;i<imgs.length;i++)
         {
            parsed[i] = new ParsedImage(imgs[i]);
         }
         ImagePair[] pairs = new ImagePair[parsed.length-1];
         for(int q=0; q<imgs.length-1;q++)
         {
            pairs[q] = new ImagePair(parsed[q],parsed[q+1]);
         }
         return pairs;
      }
      public static void classify(ImagePair[] pairs)
      {
         for(ImagePair p: pairs)
         {
            _classify_taskbar(p);
         }
      }
      public static void _classify_taskbar(ImagePair e)
      {
         BufferedImage before_taskbar = e.getBefore().getTaskbar();
         BufferedImage after_taskbar = e.getAfter().getTaskbar();
         BufferedImage imgdiff = ImageOps.diff(before_taskbar,after_taskbar);
         boolean diff = false;
      	// are there any white 'diff' pixels?
         for (int rgbval : ImageOps.flatten(ImageOps.getpixels(imgdiff))){
            if(rgbval == 255*3){
               diff = true;
               System.out.println("taskbar update between "+ e.getBefore().getName() + " and " + e.getAfter().getName());
               break;
            }
         }
      }
   }
 	   /*
   	* Image pairs that are to be analyzed for differences
   	*/
   class ImagePair{
      private ParsedImage before;
      private ParsedImage after;
      public ImagePair(ParsedImage i, ParsedImage j)
      {
         before=i;after=j;
      }
      ParsedImage getBefore(){ 
         return before;}
      ParsedImage getAfter() { 
         return after;}
   }  
   /*
	* Parsed Image
	*/
   class ParsedImage {
   /*
   * To be more efficient I could have a static edge detector instead of reallocating memory
   * but that is a-after-it-works optimization
   */
      static int IMG_WIDTH =1280;
      static int IMG_HEIGHT = 1024;
      static int IMG_HEIGHT_MAIN_CONTENT = 978;
      static int IMG_HEIGHT_TASKBAR = IMG_HEIGHT - IMG_HEIGHT_MAIN_CONTENT;
      static int IMG_WIDTH_TASKBAR_WITHOUT_TIME = 1200;
      private BufferedImage img;
      private BufferedImage mainwindow;
      private BufferedImage taskbar;
      private BufferedImage taskbar_wo_clock; //wo ~ without
      private String name;
      private String path;
      
   	/*
   	* class declarator - seperates the 'components' of a window
   	*/
      public ParsedImage(File f) throws Exception{
      
         path = f.getPath();
         name = path.substring(path.lastIndexOf('\\')+1,path.lastIndexOf('.'));
         img = ImageIO.read(f);
         mainwindow = img.getSubimage(0,0,IMG_WIDTH,IMG_HEIGHT_MAIN_CONTENT);
         taskbar = img.getSubimage(0,IMG_HEIGHT_MAIN_CONTENT,IMG_WIDTH,IMG_HEIGHT_TASKBAR);
         taskbar_wo_clock = taskbar.getSubimage(0,0,IMG_WIDTH_TASKBAR_WITHOUT_TIME,IMG_HEIGHT_TASKBAR);
      	
      }
    
    /*
    * Accessor Methods 
    */  
      public String getName(){
         return name;}
      public BufferedImage getImg(){
         return img;}
      public BufferedImage getMainWindow(){
         return mainwindow;}
      public BufferedImage getTaskbar(){
         return taskbar;}
      public BufferedImage getTaskbarwoclock(){
         return taskbar_wo_clock;}
   	
      /*
   	* Takes a file and detects edges using canny edge detection.
   	*/
      public BufferedImage edgeDetect(File f)
      { 
         CannyEdgeDetector det = new CannyEdgeDetector();
         det.setLowThreshold(0.5f);
         det.setHighThreshold(1f);
         det.setSourceImage(img);
         try{
            det.process();
         }
            catch(IllegalArgumentException e)
            {
               System.out.print("Illegal File " + f.getPath());
            }
         BufferedImage out = det.getEdgesImage();
         String outpath = f.getPath();
         outpath = outpath.substring(0,outpath.lastIndexOf("."))+ "_out.png";
         //ImageIO.write(out, "png",new File(outpath));
         return out;
      }
   
   }
   
	   /*
   	* Generic Exception if a directory rather an a file is wanted.
   	* This is because of the assumption that we are going to walk over files
   	* inside the directory.
   	*/
   class IsNotDirectoryException extends Exception{
      public IsNotDirectoryException(){
         super("A Directory was expected");
      }
   }
