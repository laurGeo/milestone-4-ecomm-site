{"filter":false,"title":"stripe.js","tooltip":"/static/js/stripe.js","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":31,"column":3},"end":{"row":31,"column":3},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":116,"mode":"ace/mode/javascript"}},"hash":"5a0c4326c90b736b5439d6eadfad1351e1715aa8","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":31,"column":3},"action":"insert","lines":["$(function() {","    $(\"#payment-form\").submit(function() {","        var form = this;","        var card = {","            number: $(\"#id_credit_card_number\").val(),","            expMonth: $(\"#id_expiry_month\").val(),","            expYear: $(\"#id_expiry_year\").val(),","            cvc: $(\"#id_cvv\").val()","        };","        ","    Stripe.createToken(card, function(status, response) {","        if (status === 200) {","            $(\"#credit-card-errors\").hide();","            $(\"#id_stripe_id\").val(response.id);","            ","            //Prevent the Credit card Details from being submitted to our server","            $(\"#id_credit_card_number\").removeAttr('name');","            $(\"#id_cvv\").removeAttr('name');","            $(\"#id_expiry_month\").removeAttr('name');","            $(\"#id_expiry_year\").removeAttr('name');","            ","            form.submit();","            ","        } else {","            $(\"#stripe-error-message\").text(response.error.message);","            $(\"#credit-card-errors\").show();","            $(\"#validate_card_btn\").attr(\"disabled\", false);","        }","    });","    return false;","    });","});"],"id":1}]]},"timestamp":1572172898521}