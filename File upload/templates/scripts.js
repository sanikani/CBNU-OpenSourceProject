// 예측 결과 요소 가져오기
var resultElement = document.getElementById('result');

// 예측 결과에 따라 스타일 변경
if (resultElement.textContent === '결막염') {
    resultElement.style.color = '#e74c3c';  // 빨간색
} else if (resultElement.textContent === '정상') {
    resultElement.style.color = '#2ecc71';  // 초록색
}
