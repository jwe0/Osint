function submit() {
    var username = document.getElementById("username").value;

    document.getElementById("title-1").innerHTML = "";
    document.getElementById("title-2").innerHTML = "";
    document.getElementById("title-3").innerHTML = "";

    document.getElementById("basic-info").innerHTML = "";
    document.getElementById("repo-info").innerHTML = "";
    document.getElementById("followers").innerHTML = ""
    



    fetch('/get', {
        method: 'POST',
        body: JSON.stringify({
            "username": username
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)

        document.getElementById("title-1").innerHTML = "Basic";

        information = data.Info

        basic = information[0]
        repos = information[1]
        foll = information[2]

        basic.forEach(function(item) {
            var li = document.createElement("li");
            var text = document.createTextNode(item);
            li.appendChild(text);

            document.getElementById("basic-info").appendChild(li)
        })

        document.getElementById("title-2").innerHTML = "Repositories";

        repos.forEach(function(item) {
            
            var mainli = document.createElement("li");
            var maintext = document.createTextNode(item[0]);
            mainli.appendChild(maintext);

            var ulnested = document.createElement("ul");

            var descli = document.createElement("li");
            var desctext = document.createTextNode(item[1]);
            descli.appendChild(desctext)
            ulnested.appendChild(descli)

            var hrefli = document.createElement("li");
            var hreftext = document.createTextNode(item[2]);
            hrefli.appendChild(hreftext)
            ulnested.appendChild(hrefli)

            mainli.append(ulnested);


            document.getElementById("repo-info").appendChild(mainli)
        })

        document.getElementById("title-3").innerHTML = "Followers";

        foll.forEach(function(item) {
            var mainli = document.createElement("li");
            var text = document.createTextNode(item)
            mainli.append(text)

            document.getElementById("followers").appendChild(mainli)
        })

        



    })


}