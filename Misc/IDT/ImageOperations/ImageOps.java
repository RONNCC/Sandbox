   package IDT.ImageOperations;

/*
* Class of helper functions. These are specialized and are not supposed to be generic. They are
* compartmentalized for readability.
*/

   import java.awt.image.BufferedImage;
   import java.util.Arrays;

   public class ImageOps {
   
      public static BufferedImage diff(BufferedImage i, BufferedImage j)
      {
         assert ((i.getWidth()==j.getWidth()) &&(i.getHeight()==j.getHeight()) && (i.getType()==j.getType())): "Image Dims / Types do not match";
         BufferedImage diff = new BufferedImage(i.getWidth(),i.getHeight(),i.getType());
         for(int q=0;q<i.getWidth();q++){
            for(int w=0;w<j.getHeight();w++){
               diff.setRGB(q,w,((i.getRGB(q,w) == j.getRGB(q,w))? 0x000000:0xFFFFFF ));
            }
         }
         return diff;
      }
    /*
    * The following methods (and the previous) are horribly inefficient, but are used since Java's getPixels ~ returning an array of pixels doesn't seem to work
    */  
   	
      public static BufferedImage binaryImage(BufferedImage img,int r,int g,int b){
         return null;
      }
      /*
   	* Unpacks an ARGB
   	*/
      public static int[] convertRGB(int argb)
      {
         return new int[]{
               (argb >> 24) & 0xFF,
               (argb >> 16) & 0xFF,
               (argb >> 8) & 0xFF,
               (argb >> 0) & 0xFF
               };
      }
    
   
      /*
      * Returns r+g+b for each pixel ~ as you can expect this has very limited use.
      */
      public static int[][] getpixels(BufferedImage i){
      
      // q is moving vertically in array
      // w moves horiz.
      // assumes 2d standard, rectangular matrix as per usual java bounds
         int[][] arr = new int[i.getHeight()][i.getWidth()];
         for(int q=0;q<i.getWidth();q++)
         {
            for(int w=0;w<i.getHeight();w++){
               int sum=0;
               int[] tmp = Arrays.copyOfRange(convertRGB(i.getRGB(q,w)),0,3);
            	
            	
               for(int e : tmp )
               
               
               {sum+=e;}
               arr[w][q]=sum;
            }
         }
         return arr;
      }  
   	
   	/*
   	* Flattens 2d array to 1d array
   	* given 2d array, it concats as what it sees as a list of rows together.
   	*/
      public static int[] flatten(int[][] arr)
      {
         int height = arr.length;
         int width = arr[0].length;
      //assumes multi dim rectangular array. 
         int[] tmp = new int[height*width];
         for(int i=0;i<height;i++){
            for(int w=0;w<width;w++){
               tmp[i+w*(i+1)]=arr[i][w];
            }
         }
         return tmp;
      }
      public static int convertARGB(int a,int r,int g,int b){
         return a << 24 + r << 16 + g<<8 + b;
      }
   }
