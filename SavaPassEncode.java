import javax.crypto.*;
import javax.crypto.spec.*;
import sun.misc.*;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class WebtopPassEncode {

    public static void main(String args[]) throws Exception {
        String p;
        try {
            p = args[0];
        } catch (ArrayIndexOutOfBoundsException e1) {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            p = br.readLine();
        } 
        String c=cipher(p,"password");
        System.out.println(c);
    }

    public static String cipher(String pass, String key) throws Exception {
        DESKeySpec ks=new DESKeySpec(key.getBytes("UTF-8"));
        SecretKey sk=SecretKeyFactory.getInstance("DES").generateSecret(ks);
        Cipher cipher=Cipher.getInstance("DES");
        cipher.init(Cipher.ENCRYPT_MODE,sk);
        return (new BASE64Encoder()).encode(cipher.doFinal(pass.getBytes("UTF-8")));
    }

}
