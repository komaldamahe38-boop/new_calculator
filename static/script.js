function calculate() {

    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let operation = document.getElementById("operation").value;

    if(num1 === "" || num2 === ""){
        alert("Please enter both numbers");
        return;
    }

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            num1: num1,
            num2: num2,
            operation: operation
        })
    })
    .then(response => response.json())
    .then(data => {

        if(data.error){
            alert(data.error);
            return;
        }

        document.getElementById("result").innerHTML =
            "Result: " + data.result;

        let historyList =
            document.getElementById("history-list");

        historyList.innerHTML = "";

        data.history.forEach(item => {
            let li = document.createElement("li");
            li.textContent = item;
            historyList.appendChild(li);
        });
    });
}
