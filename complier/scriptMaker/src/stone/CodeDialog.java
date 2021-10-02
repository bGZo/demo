package stone;

import javax.swing.*;
import java.io.*;

public class CodeDialog {
    private String buffer=null;
    private int pos=0;

    public int read(char[] cbuf, int off, int len) throws IOException{
        if(buffer==null){
            String in = showDialog();
            if (in==null)return -1;
            else {
                print(in);
                buffer=in+"\n";
                pos=0;
            }
        }
        int size=0;
        int length=buffer.length();
        while (pos<length && size<len)
            cbuf[off + size++]=buffer.charAt(pos++);//???

        if(pos==length)
            buffer=null;

        return size;
    }
    protected void print(String s) {System.out.println(s);}
    public void close() throws IOException{};
    protected String showDialog(){
        JTextArea area=new JTextArea(20,40);//??
        JScrollPane pane=new JScrollPane(area);
        int result =JOptionPane.showOptionDialog(null, pane, "Input",
                                                    JOptionPane.OK_CANCEL_OPTION,
                                                    JOptionPane.PLAIN_MESSAGE,
                                                null,null,null);
        if(result==JOptionPane.OK_OPTION) return area.getText();
        else return null;
    }
    public static Reader file() throws FileNotFoundException{
        JFileChooser chooser=new JFileChooser();
        if(chooser.showDialog(null)==JFileChooser.APPROVE_OPTION)
            return new BufferedReader(new FileReader(chooser.getSelectedFile()));
        else throw new FileNotFoundException("no file specified");
    }
}
