$(document).ready(function(){
    const CARD_DIGITS = 16;
    var cardNumber = '';

    function formatCardNumber(){
        nonNumbers = "_".repeat(CARD_DIGITS - cardNumber.length);
        rawString = nonNumbers + cardNumber;
        $("#card-num-input").val(rawString.replace(/\W/gi, '').replace(/(.{4})/g, '$1-').slice(0, -1));
    };

    formatCardNumber();

    $(".btn-ctrl").on('click', function(){
        if ($(this).val() != 'C' && $(this).val() != 'Enter' && cardNumber.length < CARD_DIGITS) {
            cardNumber += $(this).val();
        }
        if ($(this).val() == 'C') {
            cardNumber = ''
        }
        $("#card-num").val(cardNumber);
        formatCardNumber();
    });


});