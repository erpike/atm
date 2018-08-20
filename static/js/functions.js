$(document).ready(function(){
    const CARD_DIGITS = 16;
    var cardNumber = '';

    function formatNumber(){
        nonNumbers = "_".repeat(CARD_DIGITS - cardNumber.length);
        rawString = nonNumbers + cardNumber;
        $("#card-number").text(rawString.replace(/\W/gi, '').replace(/(.{4})/g, '$1-').slice(0, -1));
        console.log(cardNumber.length)
    };

    formatNumber();
    $(".btn-ctrl").on('click', function(){
        if (cardNumber.length < 16){
            cardNumber += $(this).val()
            formatNumber();
        }
    });
});