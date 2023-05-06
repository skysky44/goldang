  // 리뷰쓰기 Hover
  function onHover()
  {
      $('#ReviewIcon').attr('class', 'Detail__Title__ReviewImg--Hover')
  }

  function offHover()
  {
      $('#ReviewIcon').attr('class', 'Detail__Title__ReviewImg')
  }

  // 색 변경(기본 값)
  document.getElementById("전체_btn").style.color = '#ff7100'

  // 전체 버튼 클릭 시
  document.getElementById("전체_btn").addEventListener("click", function() {
    setButtonColor("전체_btn");
    showAllReviews();
  });

  // 맛있다 버튼 클릭 시
  document.getElementById("맛있다_btn").addEventListener("click", function() {
    setButtonColor("맛있다_btn");
    showReviews('맛있다');
  });

  // 괜찮다 버튼 클릭 시
  document.getElementById("괜찮다_btn").addEventListener("click", function() {
    setButtonColor("괜찮다_btn");
    showReviews('괜찮다');
  });

  // 별로 버튼 클릭 시
  document.getElementById("별로_btn").addEventListener("click", function() {
    setButtonColor("별로_btn");
    showReviews('별로');
  });

  // 버튼 색상 설정 함수
  function setButtonColor(activeButtonId) {
    var buttonIds = ["전체_btn", "맛있다_btn", "괜찮다_btn", "별로_btn"];
    var activeColor = '#ff7100';
    var inactiveColor = '#9b9b9b';

    buttonIds.forEach(function(buttonId) {
      var button = document.getElementById(buttonId);
      button.style.color = (buttonId === activeButtonId) ? activeColor : inactiveColor;
    });
  }

  // 전체 리뷰 출력 함수
  function showAllReviews() {
    var reviewItems = document.getElementsByClassName("review-item");
    
    // 모든 리뷰 아이템 보여주기
    for (var i = 0; i < reviewItems.length; i++) {
      reviewItems[i].style.display = 'block';
    }
  }

  // 필터별 리뷰 출력 함수
  function showReviews(tasteEvaluation) {
    var reviewItems = document.getElementsByClassName("review-item");

    // 모든 리뷰 아이템 숨기기
    for (var i = 0; i < reviewItems.length; i++) {
      reviewItems[i].style.display = 'none';
    }

    // 해당 분류의 리뷰 아이템 보여주기
    var targetItems = document.getElementsByClassName(tasteEvaluation);
    for (var j = 0; j < targetItems.length; j++) {
      targetItems[j].style.display = 'flex';
      var parentDiv = targetItems[j].parentNode;
      parentDiv.style.display = 'block';
    }
  }


  // 카카오 맵 api 이용
  var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
  mapOption = {
      center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
      level: 3 // 지도의 확대 레벨
  }

  // 지도를 생성합니다    
  var map = new kakao.maps.Map(mapContainer, mapOption)

  // 주소-좌표 변환 객체를 생성합니다
  var geocoder = new kakao.maps.services.Geocoder()

  // data-address 속성 값을 가져옵니다
  var address = mapContainer.dataset.address;

  // 주소로 좌표를 검색합니다
  geocoder.addressSearch(address, function(result, status) {

    // 정상적으로 검색이 완료됐으면 
    if (status === kakao.maps.services.Status.OK) {

      var coords = new kakao.maps.LatLng(result[0].y, result[0].x)

      // 결과값으로 받은 위치를 마커로 표시합니다
      var marker = new kakao.maps.Marker({
          map: map,
          position: coords
      })

      // 인포윈도우로 장소에 대한 설명을 표시합니다
      var infowindow = new kakao.maps.InfoWindow({
          content: '<div style="width:150px;text-align:center;padding:6px 0;"> {{ post.title }} </div>'
      });
      infowindow.open(map, marker)

      // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
      map.setCenter(coords)
    } 
  })