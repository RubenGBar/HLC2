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

public class Ejercicio2 {
	
	static WebDriver driver1;
	static String url = "http://localhost:3000/";

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
	}
	
	// Comprueba el titulo es el correspondiente
	@Test
	void testTitulo() {
		driver1.get(url);
		String titulo = driver1.getTitle();
		assertEquals("Formulario de Registro - Mi web", titulo);
	}

	// Comprueba que existe la cabecera
	@Test
	void testCabecera() {
		driver1.get(url);
		WebElement cabecera = driver1.findElement(By.id("Cabecera"));

		String textoCabecera = cabecera.getText();
		assertEquals("Formulario de Registro", textoCabecera);
	}

	// Comprueba que existe el label del nombre
	@Test
	void testLabelNombre() {
		driver1.get(url);
		WebElement texto = driver1.findElement(By.id("nombreTexto"));

		String textoLabel = texto.getText();
		assertEquals("Nombre:", textoLabel);
	}

	// Comprueba que existe el input para el nombre
	@Test
	void testInput1() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("nombreInput"));

		boolean siExiste = input.isEnabled();
		assertTrue(siExiste);
	}

	// Comprueba que el tipo del input para el nombre
	@Test
	void testTipoInput1() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("nombreInput"));
		String tipo = input.getAttribute("type");
		assertEquals("text", tipo);
	}

	// Comprueba que existe el label del apellido
	@Test
	void testLabelApellidos() {
		driver1.get(url);
		WebElement label = driver1.findElement(By.id("apellidoTexto"));

		String textoLabel = label.getText();
		assertEquals("Apellido:", textoLabel);
	}

	// Comprueba que existe el input para el apellido
	@Test
	void testInput2() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("apellidoInput"));

		boolean siExiste = input.isEnabled();
		assertTrue(siExiste);
	}

	// Comprueba que el tipo del input para el apellido
	@Test
	void testTipoInput2() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("apellidoInput"));
		String tipo = input.getAttribute("type");
		assertEquals("text", tipo);
	}

	// Comprueba que existe el label del sexo
	@Test
	void testLabelSexo() {
		driver1.get(url);
		WebElement label = driver1.findElement(By.id("sexoTexto"));

		String textoLabel = label.getText();
		assertEquals("Sexo:", textoLabel);
	}

	// Comprueba que si se pulsa un radio button el otro se deselecciona
	@Test
	void testRadioHombreTrueMujerFalse() {
		driver1.get(url);
		
		WebElement radioHombre = driver1.findElement(By.xpath("//button[@value='Hombre']"));
		radioHombre.click();
		String seleccionadoHombre = radioHombre.getAttribute("aria-checked");
		
		WebElement radioMujer = driver1.findElement(By.xpath("//button[@value='Mujer']"));
		String seleccionadoMujer = radioMujer.getAttribute("aria-checked");
		
		assertEquals("false", seleccionadoMujer);
		assertEquals("true", seleccionadoHombre);
	}
	
	// Lo mismo que el anterior, pero al revés
	@Test
	void testRadioMujerTrueHombreFalse() {
		driver1.get(url);
		
		WebElement radioMujer = driver1.findElement(By.xpath("//button[@value='Mujer']"));
		radioMujer.click();
		
		String seleccionadoMujer = radioMujer.getAttribute("aria-checked");

		WebElement radioHombre = driver1.findElement(By.xpath("//button[@value='Hombre']"));
		
		String seleccionadoHombre = radioHombre.getAttribute("aria-checked");
		assertEquals("false", seleccionadoHombre);
		assertEquals("true", seleccionadoMujer);
	}

	// Comprueba que existe el label del correo
	@Test
	void testLabelCorreo() {
		driver1.get(url);
		WebElement label = driver1.findElement(By.id("correoTexto"));

		String textoLabel = label.getText();
		assertEquals("Correo:", textoLabel);
	}

	// Comprueba que existe el input para el correo
	@Test
	void testInput3() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("correoInput"));

		boolean siExiste = input.isEnabled();
		assertTrue(siExiste);
	}

	// Comprueba que el tipo del input para el correo
	@Test
	void testTipoInput3() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("correoInput"));
		String tipo = input.getAttribute("type");
		assertEquals("text", tipo);
	}

	// Comprueba que existe una casilla de verificacion
	@Test
	void testCasillaTexto1() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkNovedades"));
		boolean siExiste = casilla.isEnabled();
		assertTrue(siExiste);
	}

	// Comprueba que el check comience en True
	@Test
	void testCasillaCheck1True() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkNovedades"));
		String valor = casilla.getAttribute("aria-checked");
		assertEquals("true", valor);
	}
	
	// Comprueba que al pulsar el check se pone en False
	@Test
	void testCasillaCheck1False() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkNovedades"));
		casilla.click();
		String valor = casilla.getAttribute("aria-checked");
		assertEquals("false", valor);
	}

	// Comprueba que existe una casilla de verificacion
	@Test
	void testCasillaLeer() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkCondiciones"));
		boolean siExiste = casilla.isEnabled();
		assertTrue(siExiste);
	}
	
	// Comprueba que el check comience en False
	@Test
	void testCasillaCheck2False() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkCondiciones"));
		String valor = casilla.getAttribute("aria-checked");
		assertEquals("false", valor);
	}
	
	// Comprueba que al pulsar el check se pone en True
	@Test
	void testCasillaCheck2True() {
		driver1.get(url);
		WebElement casilla = driver1.findElement(By.id("checkCondiciones"));
		casilla.click();
		String valor = casilla.getAttribute("aria-checked");
		assertEquals("true", valor);
	}

	// Comprueba que existe el botón de enviar datos
	@Test
	void testBoton() {
		driver1.get(url);
		WebElement input = driver1.findElement(By.id("botonEnviar"));
		boolean siExiste = input.isEnabled();
		assertTrue(siExiste);
	}

}
