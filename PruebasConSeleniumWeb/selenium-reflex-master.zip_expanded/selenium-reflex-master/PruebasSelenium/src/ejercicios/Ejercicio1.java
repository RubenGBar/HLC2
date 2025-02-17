package ejercicios;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.List;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Ejercicio1 {
	
	static WebDriver driver1;
	static WebDriver driver2;
	static WebDriver driver3;
	static WebDriver driver4;
	static WebDriver driver5;
	static WebDriver driver6;
	static WebDriver driver7;
	static String url = "http://localhost:3000/";
	
	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver2 = new ChromeDriver();
		driver3 = new ChromeDriver();
		driver4 = new ChromeDriver();
		driver5 = new ChromeDriver();
		driver6 = new ChromeDriver();
		driver7 = new ChromeDriver();
	}
	
	// Comprueba que se encuentre la cabecera del index
	@Test
	void testCabecera() {
		driver1.get(url);
		WebElement cabecera = driver1.findElement(By.id("Cabecera"));
		
		String texto = cabecera.getText();
		assertEquals("Enlaces Favoritos", texto);
	}
	
	
	// Comprueba que haya dos elementos en la lista
    @Test
    void testElementos() {
        driver1.get(url);
        WebElement lista = driver1.findElement(By.id("listaEnlaces"));
        List<WebElement> elementos = lista.findElements(By.tagName("li"));

        assertEquals(2, elementos.size());
    }
    
    // Test para clickar en el primer enlace
    @Test
    void testClickEnlace1() {
    	
    	String urlPaginaBuscadores;
    	
    	driver1.get(url);
    	WebElement enlace = driver1.findElement(By.id("enlaceBuscadores"));
    	
    	enlace.click();
    	
    	try {
    		
			Thread.sleep(500);
			
		} catch (InterruptedException e) {
			
			System.out.println(e);
			
		}
    	
    	urlPaginaBuscadores = driver1.getCurrentUrl();
    	
    	assertEquals("http://localhost:3000/Buscadores/", urlPaginaBuscadores);
    	
    }
    
    // Test para clickar en el segundo enlace
    @Test
    void testClickEnlace2() {
    	
    	String urlPaginaRedesSociales;
    	
    	driver1.get(url);
    	WebElement enlace = driver1.findElement(By.id("enlaceRedesSociales"));
    	
    	enlace.click();
    	
    	try {
    		
			Thread.sleep(500);
			
		} catch (InterruptedException e) {
			
			System.out.println(e);
			
		}
    	
    	urlPaginaRedesSociales = driver1.getCurrentUrl();
    	
    	assertEquals("http://localhost:3000/Redes_Sociales/", urlPaginaRedesSociales);
    	
    }
    
    // Comprueba que se encuentre la cabecera del index
 	@Test
 	void testCabeceraBuscadores() {
 		String texto = "";
 		
 		driver1.get(url);
 		WebElement enlace = driver1.findElement(By.id("enlaceBuscadores"));
    	
 		
    	enlace.click();
    	
    	try {
    		
			Thread.sleep(500);
			
		} catch (InterruptedException e) {
			
			System.out.println(e);
			
		}
 		
    	WebElement cabecera = driver1.findElement(By.id("Cabecera"));
 		
 		texto = cabecera.getText();
    	
 		assertEquals("Buscadores", texto);
 	}
 	
 	// Comprueba que se viaje a la página de Google
  	@Test
  	void testEnlace1Buscadores() {
  		String urlPagina = "";
  		WebElement enlace1;
  		WebElement enlace2;
  		
  		driver2.get(url);
    	
  		enlace1 = driver2.findElement(By.id("enlaceBuscadores"));
    	enlace1.click();
    	
    	try {
    		
			Thread.sleep(500);
			
		} catch (InterruptedException e) {
			
			System.out.println(e);
			
		}
    	
    	enlace2 = driver2.findElement(By.id("enlaceGoogle"));
    	enlace2.click();
    	
    	try {
    		
			Thread.sleep(500);
			
		} catch (InterruptedException e) {
			
			System.out.println(e);
			
		}
    	
    	for (String handle : driver2.getWindowHandles()) {
    	    driver2.switchTo().window(handle);
    	}
    	
    	urlPagina = driver2.getCurrentUrl();
    	
    	assertEquals("https://www.google.com/", urlPagina);
  	}
  	
  	// Comprueba que se viaje a la página de Bing
   	@Test
   	void testEnlace2Buscadores() {
   		String urlPagina = "";
   		WebElement enlace1;
   		WebElement enlace2;
   		
   		driver3.get(url);
     	
   		enlace1 = driver3.findElement(By.id("enlaceBuscadores"));
     	enlace1.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	enlace2 = driver3.findElement(By.id("enlaceBing"));
     	enlace2.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	for (String handle : driver3.getWindowHandles()) {
     	    driver3.switchTo().window(handle);
     	}
     	
     	urlPagina = driver3.getCurrentUrl();
     	
     	assertEquals("https://www.bing.com/?brdr=1", urlPagina);
   	}
   	
   	// Comprueba que se viaje a la página de Baidu
   	@Test
   	void testEnlace3Buscadores() {
   		String urlPagina = "";
   		WebElement enlace1;
   		WebElement enlace2;
   		
   		driver4.get(url);
     	
   		enlace1 = driver4.findElement(By.id("enlaceBuscadores"));
     	enlace1.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	enlace2 = driver4.findElement(By.id("enlaceBaidu"));
     	enlace2.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	for (String handle : driver4.getWindowHandles()) {
     	    driver4.switchTo().window(handle);
     	}
     	
     	urlPagina = driver4.getCurrentUrl();
     	
     	assertEquals("https://www.baidu.com/", urlPagina);
   	}
  	
   	// Comprueba que se encuentre la cabecera de la página de Redes Sociales
  	@Test
  	void testCabeceraRedesSociales() {
  		String texto = "";
  		
  		driver1.get(url);
  		WebElement enlace = driver1.findElement(By.id("enlaceRedesSociales"));
     	
  		
     	enlace.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
  		
     	WebElement cabecera = driver1.findElement(By.id("Cabecera"));
  		
  		texto = cabecera.getText();
     	
  		assertEquals("Redes Sociales", texto);
  	}
  	
  	// Comprueba que se viaje a la página de Instagram
   	@Test
   	void testEnlace1RedesSociales() {
   		String urlPagina = "";
   		WebElement enlace1;
   		WebElement enlace2;
   		
   		driver5.get(url);
     	
   		enlace1 = driver5.findElement(By.id("enlaceRedesSociales"));
     	enlace1.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	enlace2 = driver5.findElement(By.id("enlaceInstagram"));
     	enlace2.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	for (String handle : driver5.getWindowHandles()) {
     		driver5.switchTo().window(handle);
     	}
     	
     	urlPagina = driver5.getCurrentUrl();
     	
     	assertEquals("https://www.instagram.com/", urlPagina);
   	}
   	
   	// Comprueba que se viaje a la página de TikTok
   	@Test
   	void testEnlace2RedesSociales() {
   		String urlPagina = "";
   		WebElement enlace1;
   		WebElement enlace2;
   		
   		driver6.get(url);
     	
   		enlace1 = driver6.findElement(By.id("enlaceRedesSociales"));
     	enlace1.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	enlace2 = driver6.findElement(By.id("enlaceTikTok"));
     	enlace2.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	for (String handle : driver6.getWindowHandles()) {
     		driver6.switchTo().window(handle);
     	}
     	
     	urlPagina = driver6.getCurrentUrl();
     	
     	assertEquals("https://www.tiktok.com/explore", urlPagina);
   	}
   	
   	// Comprueba que se viaje a la página de Facebook
   	@Test
   	void testEnlace3RedesSociales() {
   		String urlPagina = "";
   		WebElement enlace1;
   		WebElement enlace2;
   		
   		driver7.get(url);
     	
   		enlace1 = driver7.findElement(By.id("enlaceRedesSociales"));
     	enlace1.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	enlace2 = driver7.findElement(By.id("enlaceFacebook"));
     	enlace2.click();
     	
     	try {
     		
 			Thread.sleep(500);
 			
 		} catch (InterruptedException e) {
 			
 			System.out.println(e);
 			
 		}
     	
     	for (String handle : driver7.getWindowHandles()) {
     		driver7.switchTo().window(handle);
     	}
     	
     	urlPagina = driver7.getCurrentUrl();
     	
     	assertEquals("https://www.facebook.com/", urlPagina);
   	}
}
