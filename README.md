# SP_Task_09: Kubernetes Integration with Python-CGI

## Task Description:

In continuation of task 7.1 you need to Integrate Kubernetes commands that can be run through webUI created by you. 
This time create webUI page as such that using normal English conversation your all commands can run in background. 
Example - when we write 'run deployment using httpd image' then it run complete deployment command in backend. 

Feature necessary:
<br>
-- It can launch pods with specific name given by user. <br>
-- Run deployment using image and name given by user. <br>
-- Expose services on given user input port number. <br>
-- Scale the replica according to user need. <br>
-- Delete complete environment created. <br>
-- Delete specific resources given by user. <br>
-- Extra features related to k8s ( Optional).<br>
-- This app will help the user to run all the Kubernetes commands.<br>

<hr>

## Steps to do:
### Step1: 
To execute this task we should have the Kubernetes clustre running. It can be on the Cloud or in your local system. To perform this Task I am using the minikube as the Kubernetes clustre in my local system.

![image](https://user-images.githubusercontent.com/65216265/124090812-d20b1280-da72-11eb-8539-b249d57c8650.png)

So my Minikube VM is Up and running.

### Step2:
Now we have to tell the our python cgi program that on where my Kubernetes clustre is running( IP address of your kubernetes VM ), so that it can connect and fetch the data.
So we have the `dmin.conf`file in the `etc/kubernetes` directory which contain all the info.
![image](https://user-images.githubusercontent.com/65216265/124091766-c8ce7580-da73-11eb-9b19-702219e1136c.png)
Copy this file in the cgi-bin directory of your Web-server.

### Step3:
Now clone this repo and the move the kube_index.html, style.css in Document & kube.py in the cg-bin directory respectively. Start the webserver and visit the kube_index.html.

### Step4:
In the Kube.py in line_number=10, Enter your VM IP there.

## Output:

![image](https://user-images.githubusercontent.com/65216265/124093642-accbd380-da75-11eb-9d8b-973362502ce6.png)

### Creating deployment & scaling it.

`get deployment`

![image](https://user-images.githubusercontent.com/65216265/124094093-13e98800-da76-11eb-9805-f43490fc69e8.png)

`create deployment myweb --image=httpd`
![image](https://user-images.githubusercontent.com/65216265/124094320-4d21f800-da76-11eb-84eb-e861d167dcda.png)

`get deployemnt`

![image](https://user-images.githubusercontent.com/65216265/124094502-7773b580-da76-11eb-8ca8-2e4172b50ba2.png)

`get pods`

![image](https://user-images.githubusercontent.com/65216265/124094657-9bcf9200-da76-11eb-8661-1ab68c7f43dc.png)

`scale deployment myweb --replicas=6`

![image](https://user-images.githubusercontent.com/65216265/124094897-d33e3e80-da76-11eb-8115-7c45da3685e5.png)

`get pods`

![image](https://user-images.githubusercontent.com/65216265/124095131-041e7380-da77-11eb-93e9-c1d1f0ce4be0.png)

We have Successfully created and Scaled the Deployment. Simply, we can run all the Kubernetes Command here.































