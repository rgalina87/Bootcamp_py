let answerArray = [];
let secretWord = "";
let guessArray = [];
let wordLength = 0;

function getWord() {
  secretWord = word.val();
  letters = secretWord.split('');
    for (i = 0; i < letters.length; i++) {
      $().text(letters.length);
      answerArray[i] = " * ";
      $().append(answerArray[i]);
    }
}

  let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z'];
  let showLives = document.getElementById();
  let showCatagory = document.getElementById();
  let buttons = function () {
    myButtons = document.getElementById();
    letters = document.createElement();
  for (let i = 0; i < alphabet.length; i++) {
      letters.id = [alphabet];
      list = document.createElement();
      list.id = 'letter';
      list.innerHTML = alphabet[i];
      check();
      myButtons.appendChild(letters);
      letters.appendChild(list);
    }
  }

    function result() {
    wordHolder = document.getElementById();
    correct = document.createElement();

    for (let i = 0; i < word.length; i++) {
      correct.setAttribute();
      guess = document.createElement();
      guess.setAttribute();
      if (word[i] === "-") {
        guess.innerHTML = "-";
        space = 1;
      } else {
        guess.innerHTML = "*";
      }

      geusses.push(guess);
      wordHolder.appendChild(correct);
      correct.appendChild(guess);
    }
  }
   function lives () {
    showLives.innerHTML = "You have " + lives + " lives";
    if (lives < 1) {
      showLives.innerHTML = "Game Over";
    }
    for (let i = 0; i < geusses.length; i++) {
      if (counter + space === geusses.length) {
        showLives.innerHTML = "You Win!";
      }
    }
  }
   function check () {
    list.onclick = function () {
      let geuss = (this.innerHTML);
      this.setAttribute();
      this.onclick = null;
      for (let i = 0; i < word.length; i++) {
        if (word[i] === geuss) {
          geusses[i].innerHTML = geuss;
          counter += 1;
        } 
      }
    }
  }

