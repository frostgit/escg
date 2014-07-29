package opa.interactive.uc1;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			Robot robot = new Robot();
			int mask = InputEvent.BUTTON1_DOWN_MASK;
			int y = 0;
			int x = 0;
			robot.mouseMove(x, y);
			robot.mousePress(mask);
			robot.mouseRelease(mask);
		} catch (AWTException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("end of main... exiting");
	}

}
