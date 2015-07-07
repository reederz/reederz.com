Coursera - Cryptography I
#########################

:date: 2015-07-07 11:30
:modified: 2015-07-07 11:30
:category: blog
:tags: coursera, crypto
:slug: coursera-crypto1
:authors: Justas Azna
:summary: I have recently finished Cryptography I - an online course by Prof. Dan Boneh on Coursera.org. Here's what I have learnt.

I have recently finished `Cryptography I <https://www.coursera.org/course/crypto>`_ - an introductory online course  on Cryptography by Prof. Dan Boneh of Stanford and today I received my fancy Statement of Accomplishment. It was an interesting and challenging experience. 

The course took 6 weeks and covered Stream and Block Ciphers, Message Integrity, Authenticated Encryption, Basic Key Exchange and Public Key Encryption. We have discussed several formal security definitions such as Semantic Security, Chosen Plaintext Security, Chosen Ciphertext Security, Collision Resistance; each of which were used to describe security of different cryptographic primitives. 

Each week we would have a problem set which usually consisted of multiple-choice questions and an optional programming assignment. The programming assignments were especially great: we got to break poorly used cryptography and practice using various crypto algorithms I.e. we have broken many-time-pad, exploited CBC padding oracle vulnerabilities, factored RSA modulus with poorly generated prime factors and more.

At the end of 6 weeks we had the final exam where we reviewed what we have done throughout the course. 

The main takeaways for me are:

- never roll your own crypto
- don't even try to implement crypto standards- stick to standard, peer-reviewed and battle-tested implementations
- paranoia level up

While this course is really fun, it's not something that you can do casually. It would take me 6-12 quality hours every week to watch the lectures and finish the course work. It's actually my second attempt- the first time I gave up because my schedule was too hectic and I didn't want to invest half ass effort into this (all or nothing :).

Before crypto1, I had a course on computer security in college have read books like `The Codebreakers by David Khan <https://www.goodreads.com/book/show/29608.The_Codebreakers>`_ and `Kingpin by Kevin Poulsen <https://www.goodreads.com/book/show/9319468-kingpin>`_, dabbled with hacking challenges on `HackThisSite <https://www.hackthissite.org/>`_ and had some experience from my sysadmin/webdev work. Shortly: I knew a bit more than average Joe. Well, this course made me feel like I know nothing about Crypto (in a good way) and that was a really sobering experience. It's definitely going to affect my decisions both as webdev and as a web citizen.

As a final note, I want to thank Prof. Dan Boneh- you really know your stuff and I admire your work. I look forward to `Cryptography II <https://www.coursera.org/course/crypto2>`_ in October.
