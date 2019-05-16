package Hello;

import org.w3c.dom.Document;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.helpers.DefaultHandler;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;

public class test {

    public static void main(String[] args) {
        String fileName = null;
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setValidating(true);
            DocumentBuilder builder = factory.newDocumentBuilder();
            MyHandler handler = new MyHandler();
            builder.setErrorHandler(handler);
            Document document = builder.parse(new File("手机信息.xml"));
            if (handler.errorMessage == null) {
                System.out.println("手机信息.xml是有效的！");
            } else {
                System.out.println("手机信息.xml是无效的！");
            }
        }catch (Exception e){
            System.out.println(e);
        }
    }
}

class MyHandler extends DefaultHandler {
    String errorMessage = null;

    @Override
    public void error(SAXParseException e) throws SAXException {
        errorMessage = e.getMessage();
        System.out.println("一般错误：" + errorMessage);
    }

    @Override
    public void fatalError(SAXParseException e) throws SAXException {
        errorMessage = e.getMessage();
        System.out.println("致命错误：" + errorMessage);
    }
}