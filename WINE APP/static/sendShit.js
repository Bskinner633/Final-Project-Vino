function sendShit() {
    var sulphates = $("#sulphates").val();
    var fixedAcidity = $("#fixedAcidity").val();
    var volatileAcidity = $("#volatileAcidity").val();
    var citricAcid = $("#citricAcid").val();
    var alcohol = $("#alcohol").val();
    var residualSugar = $("#residualSugar").val();
    var chlorides = $("#chlorides").val();
    var freeSulfurDioxide = $("#freeSulfurDioxide").val();
    var totalSulfurDioxide = $("#totalSulfurDioxide").val();
    var density = $("#density").val();
    var pH = $("#pH").val();

    var payload = {
        "sulphates": sulphates,
        "fixedAcidity": fixedAcidity,
        "volatileAcidity": volatileAcidity,
        "citricAcid": citricAcid,
        "alcohol": alcohol,
        "residualSugar": residualSugar,
        "chlorides": chlorides,
        "freeSulfurDioxide": freeSulfurDioxide,
        "totalSulfurDioxide": totalSulfurDioxide,
        "density": density,
        "pH": pH
    };

    $.ajax({
        type: 'POST',
        // make sure you respect the same origin policy with this url:
        // http://en.wikipedia.org/wiki/Same_origin_policy
        url: "/doShit/",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(msg) {
            alert(Object.values(msg));
        }

        //open read and use the sav file 

    });
}