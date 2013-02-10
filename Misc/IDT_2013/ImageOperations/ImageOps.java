   package IDT.ImageOperations;

/*
* Class of helper functions. These are specialized and are not supposed to be generic. They are
* compartmentalized for readability.
*/

   import java.awt.image.BufferedImage;

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
               (argb >> 24) & 0xFF
               };
      }
      public static int convertARGB(int a,int r,int g,int b){
         return a << 24 + r << 16 + g<<8 + b;
      }
   }
