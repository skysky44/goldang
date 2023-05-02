function TextLength(ReviewWriting__main__Text){
  document.getElementById("ReviewWriting__main__TextLength").innerHTML = document.getElementById("ReviewWriting__Main__Text").value.length;

  var ContinueButton = document.querySelector('.Review__Buttons__Continue')

  if (ReviewWriting__main__Text.value.length >= 1) {  
    ContinueButton.style.color = '#ff7100'
    ContinueButton.style.border = 'solid 1px #ff7100'
    ContinueButton.style.cursor = 'pointer'
  } else {
    ContinueButton.style.color = '#CBCBCB'
    ContinueButton.style.border = 'solid 1px #CBCBCB'
    ContinueButton.style.cursor = 'not-allowed'
  }

  var SubmitButton = document.querySelector('.Review__Buttons__Submit')
  
  if (ReviewWriting__main__Text.value.length >= 1) {  
    SubmitButton.style.border = '#ff7100'
    SubmitButton.style.background = '#ff7100'
    SubmitButton.style.cursor = 'pointer'
  } else {
    SubmitButton.style.border = '#E9E9E9'
    SubmitButton.style.background = '#E9E9E9'
    SubmitButton.style.cursor = 'not-allowed'
  }

  if (ReviewWriting__main__Text.value.length > 10000) {
    alert("더이상 입력이 불가능합니다.")
    ReviewWriting__main__Text.value = ReviewWriting__main__Text.value.substring(0, 9999);
    return false;
  } 
 }

// 사용중 x

 // let deliciousbtn = document.querySelector('.ReviewWriting__Main__Rating__DeliciousButton')
// let smilebtn = document.querySelector('.ReviewWriting__Main__Rating__SmileButton')
// let sadbtn = document.querySelector('.ReviewWriting__Main__Rating__SadButton')

// let deliciousimg = document.querySelector('.ReviewWriting__Main__RatingImage--Delicious')
// let smileimg = document.querySelector('.ReviewWriting__Main__RatingImage--Smile')
// let sadimg = document.querySelector('.ReviewWriting__Main__RatingImage--Sad')

// // 기본값
// deliciousbtn.style.color = '#ff7100'
// deliciousimg.classList.add('ReviewWriting__Main__RatingImage--Delicious--Active')
// deliciousimg.classList.remove('ReviewWriting__Main__RatingImage--Delicious--None')


// // 버튼 이벤트
// deliciousbtn.addEventListener('click', () => {
//     deliciousbtn.style.color = '#ff7100'
//     deliciousimg.classList.add('ReviewWriting__Main__RatingImage--Delicious--Active')
//     deliciousimg.classList.remove('ReviewWriting__Main__RatingImage--Delicious--None')

//     smilebtn.style.color = '#CDCDCD'
//     smileimg.classList.remove('ReviewWriting__Main__RatingImage--Smile--Active')
//     smileimg.classList.add('ReviewWriting__Main__RatingImage--Smile--None')

//     sadbtn.style.color = '#CDCDCD'
//     sadimg.classList.remove('ReviewWriting__Main__RatingImage--Sad--Active')
//     sadimg.classList.add('ReviewWriting__Main__RatingImage--Sad--None')
// })


// smilebtn.addEventListener('click', () => {
//   smilebtn.style.color = '#ff7100'
//   smileimg.classList.add('ReviewWriting__Main__RatingImage--Smile--Active')
//   smileimg.classList.remove('ReviewWriting__Main__RatingImage--Smile--None')

//   sadbtn.style.color = '#CDCDCD'
//   sadimg.classList.remove('ReviewWriting__Main__RatingImage--Sad--Active')
//   sadimg.classList.add('ReviewWriting__Main__RatingImage--Sad--None')

//   deliciousbtn.style.color = '#CDCDCD'
//   deliciousimg.classList.remove('ReviewWriting__Main__RatingImage--Delicious--Active')
//   deliciousimg.classList.add('ReviewWriting__Main__RatingImage--Delicious--None')
// })


// sadbtn.addEventListener('click', () => {
//   sadbtn.style.color = '#ff7100'
//   sadimg.classList.add('ReviewWriting__Main__RatingImage--Sad--Active')
//   sadimg.classList.remove('ReviewWriting__Main__RatingImage--Sad--None')

//   smilebtn.style.color = '#CDCDCD'
//   smileimg.classList.remove('ReviewWriting__Main__RatingImage--Smile--Active')
//   smileimg.classList.add('ReviewWriting__Main__RatingImage--Smile--None')

//   deliciousbtn.style.color = '#CDCDCD'
//   deliciousimg.classList.remove('ReviewWriting__Main__RatingImage--Delicious--Active')
//   deliciousimg.classList.add('ReviewWriting__Main__RatingImage--Delicious--None')
// })