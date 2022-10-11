let rdm = Math.floor(Math.random()*10)
let chances = 0
let g;

do{
let g = Number(prompt("What is your guess"))
if (g<rdm){
console.log("Your guess is smaller than rdm number")
}

else if(g>rdm){
console.log("Your guess is greater than rdm number")
}
else{
console.log("your guess is correct")
  break
}
chances+=1
}
while(g!=rdm)
console.log(`Your scoreis `+ (100 - chances))


