## Welcome to Game Center!! 

Hello! In this repository you can visit a implementation of an Hangman game and an 
Guess The Number Game.

#### _Okay, but, how it works??_

The main is [jogos](jogos.py), where user can decided with game wanna to play.
This scream appers when you run it:

<div align="center" height=100 width=250>
    <image src="./images/choose_your_game.png"></image>
</div>

After that, you can start to play...


- *Hangman Game*

A Hangman Game it is a game where it exists a word and user have to find which word is it by guessing a letter of it.
Here the lists of words is in [palavras.txt](palavras.txt) (if you wanna to put more words, please be my guest!)
<br>
<br>
<div align="center" height=100 width=250>
    <image src="./images/hangman_game.png" height=300 width=300></image>
</div>

Program will be asking to you which letter do you wanna guess. It will be advising you about your lifes (it depends in which level
are you playing), and where did the program found the letter your guessed right in the word (about the index). 

If you guess whole word without dying, this is the message it will appear in your computer:

<div align="center" height=100 width=250>
    <image src="./images/winner_hangman_game.png" height=300 width=300></image>
</div>

If you didn´t get the word, this will appear:
<div align="center" height=100 width=250>
    <image src="./images/you_lose_it.png" height=300 width=250></image>
</div>

And that´s it about hangman game!

- *Guess The Number Game*

This is the game where you keep trying to guess a number, and program will be
telling you if the number is to high or to low of a random number that you have to guess it right.

<div align="center" height=100 width=250>
    <image src="./images/guess_the_number.png" height=300 width=300></image>
</div>

It have a level dificulty to choose. The quantity of lifes you have in game, it depends on this.

This was a exercise for learning Python. Hope you like it :)

_February 2022_ | Python