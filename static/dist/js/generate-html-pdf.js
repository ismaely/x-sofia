function convertHtmlPdf() {
    const element = document.getElementById('reciboInscricao');

    var name = moment().format("DD-MM-YYYY-h:m:s");
    namefile = name + ".pdf";
    html2pdf().from(element).save(namefile);
}