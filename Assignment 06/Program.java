/**
 * @author Lane Lunsford
 * Assignment 06 - Turtle Turtle Turtle
 */
import java.util.Scanner;
import java.awt.Color;
public class Program{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int count;
		int shapes;
		double angle;
		System.out.println("Enter how many sides do you want your polygon to be? ");
		shapes = in.nextInt();
		Turtle turtle;
		turtle = new Turtle();
		angle = 360 / shapes;
		count = shapes;
		polygon(angle, turtle, count);	
	}
	/**
	 * Prints polygon using user imput
	 * @param angle is how many degrees turtle turns each recursion
	 * @param turtle is to draw the polygon
	 * @param count is used to avoid creating an infinite loop
	 */
	public static void polygon(double angle, Turtle turtle, int count){
		if(count > 0){
			turtle.forward(50);
			turtle.left(angle);
			polygon(angle, turtle, count - 1);
		}
	}
}
