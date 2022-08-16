<a id="test_btn1" class="waves-effect waves-light btn">button</a>
<a class="waves-effect waves-light btn"><i class="material-icons left">cloud</i>button</a>
<a class="waves-effect waves-light btn"><i class="material-icons right">cloud</i>button</a>
<script type="text/javascript" src="{{ url_for('static', filename='js/script1.js') }}"></script>

const btn = document.getElementById('test_btn1');
btn.addEventListener("click", testFxn);

function testFxn() {
    console.log("Test console messsage");
    alert ("Test Alert!");
}