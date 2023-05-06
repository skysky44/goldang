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
