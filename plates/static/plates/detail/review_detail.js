var imgBoxes = document.querySelectorAll('.Detail__Review__Detail__ImgBox');
var modalImage = document.querySelector('#ReviewDetailImg .Review__Detail__CarouselImg');
var prevButton = document.querySelector('.carousel-control-prev');
var nextButton = document.querySelector('.carousel-control-next');
var indicators = document.querySelectorAll('.Carousel__Indicators button');

// 이미지 박스 클릭 시 해당 이미지를 모달에 출력
imgBoxes.forEach(function(imgBox) {
  imgBox.addEventListener('click', function() {
    var modalCarousel = document.querySelector('#ReviewDetailImgIndicators');
    var modalImages = modalCarousel.querySelectorAll('.Review__Detail__CarouselImg');
    var selectedImageUrl = this.querySelector('.Detail__Review__Detail__Img').src;
    

    // 선택한 이미지의 인덱스를 찾기 위해 Array.from을 사용하여 modalImages를 배열로 변환
    var activeIndex = Array.from(modalImages).findIndex(function(image) {
      return image.src === selectedImageUrl;
    });
    
    // Bootstrap 모달 이미지를 업데이트하기 위해 active 클래스 설정
    modalImages.forEach(function(image) {
      image.parentNode.classList.remove('active');
    });
    
    // 선택한 이미지의 부모 클래스에 active 추가
    modalImages[activeIndex].parentNode.classList.add('active');
    

    // Bootstrap 모달 열기
    $('#ReviewDetailImg').modal('show');

    // Review__Detail__FooterImgbox의 자식 button에서 active 클래스 제거 및 active-none 클래스 추가
    var footerImgBoxes = document.querySelectorAll('.Review__Detail__FooterImgbox');
    footerImgBoxes.forEach(function(box) {
      var button = box.querySelector('button');
      if (button.classList.contains('active')) {
        button.classList.remove('active');
        button.classList.add('active-none');
        button.setAttribute('aria-current', 'false');
      }
    });

    // 선택한 이미지와 일치하는 Review__Detail__FooterImg의 부모 버튼에 active 클래스 및 aria-current 추가
    var matchingButton = document.querySelector('.Review__Detail__FooterImgbox button[data-bs-slide-to="' + activeIndex + '"]');
    
    if (matchingButton) {
      matchingButton.classList.add('active');
      matchingButton.classList.remove('active-none');
      matchingButton.setAttribute('aria-current', 'true');
    }

    // 그 외의 Review__Detail__FooterImg의 부모 버튼에 active-none 클래스 추가 및 aria-current 제거
    var nonMatchingButtons = document.querySelectorAll('.Review__Detail__FooterImgbox button:not([data-bs-slide-to="' + activeIndex + '"])');
    
    nonMatchingButtons.forEach(function(button) {
      button.classList.add('active-none');
      button.setAttribute('aria-current', 'false');
    });

    // 페이지 로드 시 초기 설정
    var activeSlide = prevcarousel.querySelector('.carousel-item.active');
    var isFirstSlide = activeSlide && activeSlide.dataset.bsSlideTo === '0';
    
    if (isFirstSlide) {
    prevButton2.style.display = 'none'; // 이전(prev) 버튼 숨기기
    } else {
    prevButton2.style.display = 'block'; // 이전(prev) 버튼 보이기
    }
    
    var lastIndex = prevcarousel.querySelectorAll('.carousel-item').length - 1;
    var isLastSlide = activeSlide && activeSlide.dataset.bsSlideTo === lastIndex.toString();
    
    if (isLastSlide) {
    nextButton2.style.display = 'none'; // 다음(next) 버튼 숨기기
    } else {
    nextButton2.style.display = 'block'; // 다음(next) 버튼 보이기
    }
  });
});

// 이전 버튼 클릭 시 다음 버튼 활성화 처리
prevButton.addEventListener('click', function() {
  var footerImgBoxes = document.querySelectorAll('.Review__Detail__FooterImgbox');
  var activeButton = null;

  footerImgBoxes.forEach(function(box) {
    var button = box.querySelector('button');
    if (button.classList.contains('active')) {
      activeButton = button;
    }
    button.classList.remove('active');
    button.classList.add('active-none');
    button.setAttribute('aria-current', 'false');
  });

  if (activeButton !== null) {
    var prevIndex = parseInt(activeButton.getAttribute('data-bs-slide-to')) - 1;
    var prevButton = document.querySelector('.Review__Detail__FooterImgbox button[data-bs-slide-to="' + prevIndex + '"]');
    prevButton.classList.remove('active-none');
    prevButton.classList.add('active');
    prevButton.setAttribute('aria-current', 'true');
  }
});

// 다음 버튼 클릭 시 다음 버튼 활성화 처리
nextButton.addEventListener('click', function() {
  var footerImgBoxes = document.querySelectorAll('.Review__Detail__FooterImgbox');
  var activeButton = null;

  footerImgBoxes.forEach(function(box) {
    var button = box.querySelector('button');
    if (button.classList.contains('active')) {
      activeButton = button;
    }
    button.classList.remove('active');
    button.classList.add('active-none');
    button.setAttribute('aria-current', 'false');
  });

  console.log(footerImgBoxes)
  
  if (activeButton !== null) {
    var nextIndex = parseInt(activeButton.getAttribute('data-bs-slide-to')) + 1;
    var nextButton = document.querySelector('.Review__Detail__FooterImgbox button[data-bs-slide-to="' + nextIndex + '"]');
    nextButton.classList.remove('active-none');
    nextButton.classList.add('active');
    nextButton.setAttribute('aria-current', 'true');
  }
});

// 이미지 버튼 클릭 시 해당 버튼 활성화 처리
indicators.forEach(function(button) {
  button.addEventListener('click', function() {
    indicators.forEach(function(btn) {
      btn.classList.remove('active');
      btn.classList.add('active-none');
      btn.setAttribute('aria-current', 'false');
    });

    button.classList.remove('active-none');
    button.classList.add('active');
    button.setAttribute('aria-current', 'true');
  });
});

// 슬라이드 이동 시 이전/다음 버튼 숨기기/보이기 처리
var prevcarousel = document.querySelector('#ReviewDetailImgIndicators');
var prevButton2 = prevcarousel.querySelector('.carousel-control-prev');
var nextcarousel = document.querySelector('#ReviewDetailImgIndicators');
var nextButton2 = nextcarousel.querySelector('.carousel-control-next');

prevcarousel.addEventListener('slide.bs.carousel', function(event) {
  var isFirstSlide = event.to === 0;
  if (isFirstSlide) {
    prevButton2.style.display = 'none'; // 이전(prev) 버튼 숨기기
    } else {
    prevButton2.style.display = 'block'; // 이전(prev) 버튼 보이기
    }
});
    
nextcarousel.addEventListener('slide.bs.carousel', function(event) {
  var totalSlides = event.relatedTarget.parentElement.children.length;
  var isLastSlide = event.to === totalSlides - 1;
  
  if (isLastSlide) {
  nextButton2.style.display = 'none'; // 다음(next) 버튼 숨기기
  } else {
  nextButton2.style.display = 'block'; // 다음(next) 버튼 보이기
  }
});