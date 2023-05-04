// function onHover()
// {
//     $('#ReviewIcon').attr('class', 'Detail__Title__ReviewImg--Hover')
// }

// function offHover()
// {
//     $('#ReviewIcon').attr('class', 'Detail__Title__ReviewImg')
// }

// // 리뷰 필터링
// // 색 변경(기본 값)
// document.getElementById("전체_btn").style.color = '#ff7100'

// // 페이지가 로드될 때 실행 (기본 값)
// $(document).ready(function() {
//   var page = 2; // 다음 페이지 번호
//   var totalPages = '{{ page_obj.paginator.num_pages }}'; // 전체 페이지 수
//   var loadedReviews = []; // 이미 로드된 리뷰 ID를 저장할 배열

//   // 최초에 리뷰가 5개만 보이도록 설정
//   var $reviews = $("#reviews_test .Detail__Review__List");
//   $reviews.hide();
//   $reviews.slice(0, 5).show();

//   // 초기 리뷰 로드 시 리뷰 ID 저장
//   $reviews.slice(0, 5).each(function() {
//     var reviewId = $(this).attr('data-review-id');
//     loadedReviews.push(reviewId);
//   });

//   // 더보기 버튼 클릭 시
//   $(document).on("click", "#load_more_reviews", function(event) {
//     event.preventDefault();

//     if (page <= totalPages) {
//       $.ajax({
//         url: "{% url 'plates:detail' post.pk %}",
//         data: { page: page },
//         success: function(response) {
//           var $newReviews = $(response).find('#reviews_test .Detail__Review__List');
//           var count = 0;

//           $newReviews.each(function() {
//             var reviewId = $(this).attr('data-review-id');

//             // 중복된 리뷰인지 확인
//             if (!loadedReviews.includes(reviewId) && count < 5) {
//               $("#reviews_test").append($(this));
//               loadedReviews.push(reviewId);
//               count++;
//             }
//           });

//           page++;
          
//         },
//         error: function(xhr, status, error) {
//           console.error(error);
//         }
//       });
//     }
//   });
// });

// // 전체 버튼 클릭 시
// document.getElementById("전체_btn").addEventListener("click", function() {
//   document.getElementById("전체_btn").style.color = '#ff7100'
//   document.getElementById("맛있다_btn").style.color = '#9b9b9b'
//   document.getElementById("괜찮다_btn").style.color = '#9b9b9b'
//   document.getElementById("별로_btn").style.color = '#9b9b9b'
//   showAllReviews();
// });

// // 전체 리뷰 출력 함수
// function showAllReviews() {
//   var reviewItems = document.getElementsByClassName("review-item");

//   // 모든 리뷰 아이템 보여주기
//   for (var i = 0; i < reviewItems.length; i++) {
//     reviewItems[i].style.display = 'block';
//   }
// }

// // 맛있다 버튼 클릭 시
// document.getElementById("맛있다_btn").addEventListener("click", function() {
//   document.getElementById("전체_btn").style.color = '#9b9b9b'
//   document.getElementById("맛있다_btn").style.color = '#ff7100'
//   document.getElementById("괜찮다_btn").style.color = '#9b9b9b'
//   document.getElementById("별로_btn").style.color = '#9b9b9b'
//   showReviews('맛있다');    
// });

// // 괜찮다 버튼 클릭 시
// document.getElementById("괜찮다_btn").addEventListener("click", function() {
//   document.getElementById("전체_btn").style.color = '#9b9b9b'
//   document.getElementById("맛있다_btn").style.color = '#9b9b9b'
//   document.getElementById("괜찮다_btn").style.color = '#ff7100'
//   document.getElementById("별로_btn").style.color = '#9b9b9b'
//   showReviews('괜찮다');   
// });

// // 별로 버튼 클릭 시
// document.getElementById("별로_btn").addEventListener("click", function() {
//   document.getElementById("전체_btn").style.color = '#9b9b9b'
//   document.getElementById("맛있다_btn").style.color = '#9b9b9b'
//   document.getElementById("괜찮다_btn").style.color = '#9b9b9b'
//   document.getElementById("별로_btn").style.color = '#ff7100'
//   showReviews('별로');        
// });

// // 필터별 리뷰 출력 함수
// function showReviews(tasteEvaluation) {
//   var reviewItems = document.getElementsByClassName("review-item");

//   // 모든 리뷰 아이템 숨기기
//   for (var i = 0; i < reviewItems.length; i++) {
//     reviewItems[i].style.display = 'none';
//   }

//   // 해당 분류의 리뷰 아이템 보여주기
//   var targetItems = document.getElementsByClassName(tasteEvaluation);
//   for (var j = 0; j < targetItems.length; j++) {
//     targetItems[j].style.display = 'flex';
//     var parentDiv = targetItems[j].parentNode;
//     parentDiv.style.display = 'block';
//   }
// }

// // $(document).ready(function() {
// //   var page = 2; // 다음 페이지 번호
// //   if (tasteEvaluation === '맛있다') {
// //     var totalPages = {{ num_pages1 }};
// //   } else if (tasteEvaluation === '괜찮다') {
// //     var totalPages = {{ num_pages2 }};
// //   } else if (tasteEvaluation === '별로') {
// //     var totalPages = {{ num_pages3 }};
// //   }
// //   var loadedReviews = []; // 이미 로드된 리뷰 ID를 저장할 배열

// //   console.log(totalPages)

// //   // 최초에 리뷰가 5개만 보이도록 설정
// //   if (tasteEvaluation === '맛있다') {
// //     var $reviews = $("#reviews_test .Detail__Review__List .맛있다");
// //   } else if (tasteEvaluation === '괜찮다') {
// //     var $reviews = $("#reviews_test .Detail__Review__List .괜찮다");
// //   } else if (tasteEvaluation === '별로') {
// //     var $reviews = $("#reviews_test .Detail__Review__List .별로");
// //   }
// //   $reviews.hide();
// //   $reviews.slice(0, 5).show();

// //   console.log($reviews.slice(0, 5))

// //   // 초기 리뷰 로드 시 리뷰 ID 저장
// //   $reviews.slice(0, 5).each(function() {
// //     var reviewId = $(this).attr('data-review-id');
// //     loadedReviews.push(reviewId);
// //   });

// //   // 더보기 버튼 클릭 시
// //   $(document).on("click", "#load_more_reviews", function(event) {
// //     event.preventDefault();

// //     if (page <= totalPages) {
// //       $.ajax({
// //         url: "{% url 'plates:detail' post.pk %}",
// //         data: { page: page },
// //         success: function(response) {
// //           if (tasteEvaluation === '맛있다') {
// //             var $newReviews = $(response).find('#reviews_test .Detail__Review__List .맛있다');
// //           } else if (tasteEvaluation === '괜찮다') {
// //             var $newReviews = $(response).find('#reviews_test .Detail__Review__List .괜찮다');
// //           } else if (tasteEvaluation === '별로') {
// //             var $newReviews = $(response).find('#reviews_test .Detail__Review__List .별로');
// //           }
// //           console.log($newReviews)
// //           var count = 0;

// //           $newReviews.each(function() {
// //             var reviewId = $(this).attr('data-review-id');
// //             console.log(reviewId)

// //             // 중복된 리뷰인지 확인
// //             if (!loadedReviews.includes(reviewId) && count < 5) {
// //               $("#reviews_test").append($(this));
// //               loadedReviews.push(reviewId);
// //               count++;
// //             }
// //           });
// //           console.log(loadedReviews)
// //           page++;
          
// //         },
// //         error: function(xhr, status, error) {
// //           console.error(error);
// //         }
// //       });
// //     }
// //   });
// // });


// // 카카오 맵 api 이용
// var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
// mapOption = {
//     center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
//     level: 3 // 지도의 확대 레벨
// }

// // 지도를 생성합니다    
// var map = new kakao.maps.Map(mapContainer, mapOption)

// // 주소-좌표 변환 객체를 생성합니다
// var geocoder = new kakao.maps.services.Geocoder()

// // 주소로 좌표를 검색합니다
// geocoder.addressSearch('{{ post.address }}', function(result, status) {

//   // 정상적으로 검색이 완료됐으면 
//   if (status === kakao.maps.services.Status.OK) {

//     var coords = new kakao.maps.LatLng(result[0].y, result[0].x)

//     // 결과값으로 받은 위치를 마커로 표시합니다
//     var marker = new kakao.maps.Marker({
//         map: map,
//         position: coords
//     })

//     // 인포윈도우로 장소에 대한 설명을 표시합니다
//     var infowindow = new kakao.maps.InfoWindow({
//         content: '<div style="width:150px;text-align:center;padding:6px 0;"> {{ post.title }} </div>'
//     });
//     infowindow.open(map, marker)

//     // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
//     map.setCenter(coords)
//   } 
// })