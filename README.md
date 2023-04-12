## Components of my solution:
### 1. Digital Ocean:
  For this assignment I had to create a VPS on Digital Ocean. A VPS is a Virtual Private Server, which is called a droplet by Digital Ocean. This droplet is necessary
  to create the continous deployment pipeline.  
  The droplet was easy to create, learning to work with the console involved some trial and error, but after a while I grew more familiar with it. To make everything
  work it involved some installing of programs like: nano, python, pip, flask, nginx, gunicorn, etc.  

### 2. Linux:
  Linux is an operating system where the droplet of Digital Ocean runs on. So by working with Digital Ocean and Ubuntu you are also working with Linux. Linux can be 
  used through a command-line interface. In an other assignment CLI was already used, but througout this assignment I got more of an understanding of what is does.
  
### 3. SSH-Keys
  SSH keys are a secure and convenient way to authenticate remote access to a server or other networked device. It is a method of authenticating access to a 
  server using public-key cryptography. You can generate SSH keys on a client machine and it has a public key and a private key. The private key is kept secret and
  should never be shared with anyone, and the public key can be 'public'. When you attempt to access a server, the client machine sends the public key to the 
  server, which then uses it to encrypt a message. You then use the private key to decrypt the challenge message and send it back to the server. If the decrypted
  message matches the original, you are granted access. In this case we use it to create a continous deployment pipeline with Github Actions. 

## Problems I had to deal with:
1. Working with Digital Ocean, I had a few problems. I couln't log on to the console because it didn't have enough memory. So I had to resize before I could do 
  anything else. A little strange I guess. Later on in the process I couldn't log in for some reason and when I tried to submit a ticket to solve the problem, you had
  to be logged in to submit a ticket. It was a strange loop. Ultimately I changed my password and that got me in.

2. I knew I had to clone my repository but I just couldn't figure out where it had to be cloned to. It is strange to learn that sometimes the 'wires' in my brain just
  don't seem to connect, but then, all at once, they do and you see what it's about. After that, when you look back, you can't see why you couldn't figure it out in
  the first place.

