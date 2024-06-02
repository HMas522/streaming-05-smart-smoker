# streaming-05-smart-smoker

# Student: Hayley M
# Date: 27May24

> Use RabbitMQ to distribute tasks to multiple workers

One process will create task messages. Multiple worker processes will share the work. 


## Before You Begin

1. Fork this starter repo into your GitHub.
1. Clone your repo down to your machine.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment. 

## Read

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
1. Read the code and comments in this repo.

## RabbitMQ Admin 

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

## Execute the Producer

1. Run emitter_of_tasks.py (say y to monitor RabbitMQ queues)

Explore the RabbitMQ website.

## Execute a Consumer / Worker

1. Run listening_worker.py

Will it terminate on its own? How do you know? 

## Ready for Work

1. Use your emitter_of_tasks to produce more task messages.

## Start Another Listening Worker 

1. Use your listening_worker.py script to launch a second worker. 

Follow the tutorial. 
Add multiple tasks (e.g. First message, Second message, etc.)
How are tasks distributed? 
Monitor the windows with at least two workers. 
Which worker gets which tasks?


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

> Get started with RabbitMQ, a message broker, that enables multiple processes to communicate reliably through an intermediary.

This project requires some free code - beyond that available in the Python Standard Library. To avoid messing up our local default Python installation, and any other Python projects we may have, we  create a local virtual environment to install and use these libraries.

Think of a virtual environment as a safe sandbox. 
We can install whatever we want in our sandbox, and it won't break other Python projects that may require different versions, etc. 

We use the built-in Python utility `venv` to create our virtual environment. 
There are other options, but this is simplest and most common. 
We create the environment as a subfolder of this repo named .venv to keep it away from our project code. 


## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)
1. RabbitMQ Server installed and running locally

## Before You Begin

1. Fork this starter repo into your GitHub account.
1. Clone your repo down to your machine.
1. Explore your new project repo in VS Code on your local machine.

## Task 1. Create a Python Virtual Environment

We will create a local Python virtual environment to isolate our project's third-party dependencies from other projects.

1. Open a terminal window in VS Code.
1. Use the built-in Python utility venv to create a new virtual environment named `.venv` in the current directory.

```shell
python -m venv .venv
```

Verify you get a new .venv directory in your project. 
We use .venv as the name to keep it away from our project files. 

## Task 2. Activate the Virtual Environment

In the same VS Code terminal window, activate the virtual environment.

- On Windows, run: `.venv\Scripts\activate`
- On Linux/MacOS, run: `source .venv/bin/activate`

Verify you see the virtual environment name (.venv) in your terminal prompt.

## Task 3. Install Dependencies into the Virtual Environment

To work with RabbitMQ, we need to install the pika library.
A library is a collection of code that we can use in our own code.
Learning to use free libraries that others have written to make our projects easier, faster, more reliable is a key skill for a developer.

We keep the list of third-party libraries needed in a file named requirements.txt.
Use the pip utility to install the libraries listed in requirements.txt into our active virtual environment. 

Make sure you can see the .venv name in your terminal prompt before running this command.

`python -m pip install -r requirements.txt`

## Task 4. Verify Setup (OPTIONAL - ONLY WORK ON SOME CONFIGURATIONS)

In your VS Code terminal window, run the following commands to help verify your setup.
These util files MAY be helpful to ensure you're setup correctly. 
You may have a different configuration and RabbitMQ may still work; the check looks in common places, but may not work for all installations. 
They are meant to be helpful, but are not required.

You can help by updating the code for other common configurations. 
Just fork the current repo, add your change, and create a pull request (no other changes please) and I'll pull it back in. 

```shell
python util_about.py
python util_aboutenv.py
python util_aboutrabbit.py
pip list
```


## Task 5. Read

1. Read the [RabbitMQ Hello World! tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
1. Read the code and comments in our 2 project files: emit_message.py and listen_for_messages.py

Don't worry if it doesn't all make sense the first time. 
Approach it like a puzzle and see what you can figure out. 

## Task 6. Execute the Producer/Sender

1. Read v1_emit_message.py (and the tutorial)
1. Run the file. 

It will run, emit a message to the named RabbitMQ queue, and finish.
We can execute additional commands in the terminal as soon as it finishes. 

## Task 7. Execute the Consumer/Listener - Execute at a later date 

1. Read v1_listen_for_messages.py (and the tutorial)
1. Run the file.

You'll need to fix an error in the program to get it to run.
Once it runs successfully, will it terminate on its own? How do you know? 
As long as the process is running, we cannot use this terminal for other commands. 

## Task 8. Open a New Terminal / Emit More Messages

1. Open a new terminal window.
1. Use this new window to run emit_message.py again.
1. Watch the listing terminal - what do you see?  A second message?

Sending the same message each time is kind of boring. This time:

1. Where is the message defined? How can you change it?
1. Modify emit_message.py to emit a different message. 
1. Execute the updated emit_message.py. 
1. Watch what happens in the listening terminal.

Repeat this process several times - emit at least 4 different messages.
Don't worry - it's just code. We can always revert back (try the 'undo' command in VS Code) to a version that works. You can't hurt anything.

## Screenshot - Documentation

![verifying setup](./images/verifying.png)

![verifying 2 setup](./images/verifying2.png)

# Created producer

1. created new .py file with student initials
2. Repurpose code from bonus. This code can read a csv file and send it as a message.
3. Open and configure conda prompt. 
4. cd Documents/streaming-05-smart-smoker
    dir
    conda activate base
5. execute hm_producer.py in conda prompt
6. Verify RabbitMQ 
7. The logger documents what messages have been received. 
8. Wait to create consumer to listen for the message. 

![Module 5 Rabbit MQ](./images/rabbitMQ.png)

![Module 5 CSV](./images/food_csv.png)

![Module 5 log](./images/food_log.png)

## Producer Implementation Questions/Remarks
1. Will you use a file docstring at the top? Yes, added student name and date - [x]
2. Where do imports go? right after the file/module docstring - [x]
3. After imports, declare any constants. 
4. After constants, define functions. - [x]
5. Define a function to offer the RabbitMQ admin site, use variables to turn it off temporarily if desired. - [x]
6. Define a main function to connect, get a communication channel, use the channel to queue_delete() all 3 queues 
    use the channel to queue_declare() all 3 queues - [x]
    open the file, get your csv reader, for each row, use the channel to basic_publish() a message - [x]
7. Use the Python idiom to only call  your functions if this is actually the program being executed (not imported). 
8. If this is the program that was called: call your offer admin function() - [x]
    call your main() function, passing in just the host name as an argument (we don't know the queue name or message yet) - [x]
 

## Handle User Interrupts Gracefully
1. Will this process be running for a while (half sec per record)?
2. If so, modify the code the option for the user to send a Keyboard interrupt (see earlier projects) - [x]

## Guided Producer Design 
1. If this is the main program being executed (and you're not importing it for its functions),
2. We should call a function to ask the user if they want to see the RabbitMQ admin webpage. - [x]
3. We should call a function to begin the main work of the program.
4. As part of the main work, we should
    1. Get a connection to RabbitMQ, and a channel, delete the 3 existing queues (we'll likely run this multiple times), and then declare them anew. 
    2. Open the csv file for reading (with appropriate line endings in case of Windows) and create a csv reader. - [x]
    3. For data_row in reader:
    [0] first column is the timestamp - we'll include this with each of the 3 messages below - [x]
    [1] Channel1 = Smoker Temp --> send to message queue "01-smoker" - [x]
    [2] Channe2 = Food A Temp --> send to message queue "02-food-A" - [x]
    [3] Channe3 = Food B Temp --> send to message queue "03-food-B" - [x]
    Send a tuple of (timestamp, smoker temp) to the first queue - [x]
    Send a tuple of (timestamp, food A temp) to the second queue - [x]
    Send a tuple of (timestamp, food B temp) to the third queue - [x]
    Create a binary message from our tuples before using the channel to publish each of the 3 messages.
    Messages are strings, so use float() to get a numeric value where needed
    Remember to use with to read the file, or close it when done.  [x]
 

## Producer Design Questions
1. Can the open() function fail? - Yes, but one might not know, with out error handling
2. What do we do if we know a statement can fail? Hint: try/except/finally - Used 3 except statements
3. Does our data have header row? - Yes, it is our time (UTC), Channel1, Channel2, Channel3
4. What happens if we try to call float("Channel1")? - Channel1 is a float, from defintion: class float - convert a string or number to a floating point number, if possible
5. How will you handle the header row in your project? - Used for data_row in reader, then tied the header and our queues/channels together. 
6. Will you delete it (easy), or use code to skip it (better/more difficult) - Did not delete. 