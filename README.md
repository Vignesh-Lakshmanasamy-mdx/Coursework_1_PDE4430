# Coursework_1_PDE4430
step 1:

Please copy the folder (Coursework1) from github or from Zip folder

step2 2:

Please paste the folder inside >>> ros ->catkin_ws->src

step 3:

Please donot change any file names and copy the below code to the terminal 
-go to Coursework1(folder) -> scripts and open terminal form that folder

step 4:

copy and paste the following comments

            chmod +x teleopration_qt.py
            chmod +x autonomous_navigation.py
            chmod +x avoid_wall.py
            chmod +x Vaccum_cleaner.py
            chmod +x multiple_vacuum_cleaner.py
            chmod +x Task5Cleaner1.py
            chmod +x Task5Cleaner2.py
            chmod +x Task5Cleaner3.py 
            chmod +x Task5Cleaner4.py

Above commands are to make the python program executable

step 5: 


To run the Task follow the below comments

->Task1 - Teleoperation using the keyboard, with an option to change movement speed

          roslaunch Coursework1 teleoperation.launch

->Task2 - Autonomous Navigation

          roslaunch Coursework1 autonomous_navigation.launch
 
->Task3 - Avoid wall collision

          roslaunch Coursework1 avoid_wall.launch

->Task4 - Vacuum cleaning behaviour

          roslaunch Coursework1 vaccum_cleaner.launch

->Task5 - Multiple turtle Vacuum cleaning behaviour

          roslaunch Coursework1 multipleturtle.launch


Note : if you have not installed pyqt ->  

           sudo apt-get install python3-pyqt5 

****************************************************************************************************


Task working description:



Task1 : Teleoperation 

demos Video link : https://youtu.be/dekssTNoz0Q

following UI contains the control elements for the teleoperation

![Screenshot 2024-11-23 000130](https://github.com/user-attachments/assets/ce09ae03-2e7b-4d92-bc22-4e713062506f)

Rqt - graph shows the node and topic used

![Screenshot 2024-11-23 000805](https://github.com/user-attachments/assets/7d76e0cf-b3f5-4e42-82e8-7ac9b839a631)

************************************************************************************************************

Task2 : Autonomous Navigation to any given coordinates

demo video link : https://youtu.be/hKF14pULE-Q

In the form enter the origin point and target point - click spwan to create the turtle on origin point and click "move to target"

![Screenshot 2024-11-23 001042](https://github.com/user-attachments/assets/2508c8ad-82ea-46b0-9248-5da15c166598)

Rqt graph shows the node and topic used

![Screenshot 2024-11-23 001114](https://github.com/user-attachments/assets/c8ad0428-fe4d-4d7b-b96a-9fb32bc1a3b1)

************************************************************************************************************

Task 3 : Avoiding the Wall collision

demo video link : https://youtu.be/2nxRpr9RtF4

in the form select the method of wall collision avoidance by rotation or by turning - and run the format reverse motion once the turtle enters the boundary it goes to wall collision avoidance mode

![Screenshot 2024-11-23 001714](https://github.com/user-attachments/assets/67653e9a-4757-4d10-aaf5-a11f32150bf6)

rqt graph for the task3 shows the nodes and topic used

![Screenshot 2024-11-23 001737](https://github.com/user-attachments/assets/38673204-251e-45e4-ad22-2794e735bd8b)

************************************************************************************************************

Task 4 : Vacuum cleaner behaviour

demo video link : https://youtu.be/wfacA-VUn0s

its simple ui, there is only two push button - one to start the turtle and another one is to reset the turtle window (reset works only after when the turtle is stopped)

![Screenshot 2024-11-23 002355](https://github.com/user-attachments/assets/c765022e-b439-42ef-b0d6-e6b91d967ab5)

Rqt graph shows the node and topic used

![Screenshot 2024-11-23 002423](https://github.com/user-attachments/assets/bfc5a014-a542-47c4-a2e3-464a96291df2)

vacuum cleaners path 

![Screenshot 2024-11-23 002628](https://github.com/user-attachments/assets/f4a0560c-9ab7-4f8e-bd04-e4e6a491915e)

************************************************************************************************************

Task 5 : Multiple Vacuum behaviour

demo Video link : https://youtu.be/v4LJpupj6ac 

 In the ui form - user need to enter the number of robots as 4 (only for 4 turtle programmed and other options for future work) and click "start the cleaner" to run the turtle

 ![Screenshot 2024-11-23 003250](https://github.com/user-attachments/assets/09c4c415-065e-465b-b0e9-167fb81218b3)

 rqt graph shows the topics and node used, here we run 4 turtle so the graph looks like this

 
 ![Screenshot 2024-11-23 003330](https://github.com/user-attachments/assets/abb1164e-be07-4463-86b7-38d2b2ad643f)


Turtlesim window with the cleaner path
 
![Screenshot 2024-11-23 003646](https://github.com/user-attachments/assets/929c370f-ca42-4e97-b724-4888bc44556c)

************************************************************************************************************
