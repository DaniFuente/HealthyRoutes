function changeTab(n){
	if(n==0){
		document.getElementById("login-tab").attributes[2].value = "col-sm-6 text-center pestañas-login-1";
		document.getElementById("register-tab").attributes[2].value = "col-sm-6 text-center pestañas-login-2 non-active";
		if(document.getElementById("pwd2") != null){
			document.getElementById("pwd2").remove();
			document.getElementById("nick").remove();
			document.getElementById("submit-button").textContent = "Iniciar Sesión";
		}
	}else{
		if(document.getElementById("pwd2") == null){
			document.getElementById("login-tab").attributes[2].value = "col-sm-6 text-center pestañas-login-1 non-active";
			document.getElementById("register-tab").attributes[2].value = "col-sm-6 text-center pestañas-login-2";
			addPwd2();
			addNick();
			document.getElementById("submit-button").textContent = "Registrarse";
		}
	}
}

function addPwd2(){
	var pwd2 = document.createElement("INPUT");
	pwd2.setAttribute("id", "pwd2");
	pwd2.setAttribute("name", "pwd2")
	pwd2.setAttribute("type", "password");
	pwd2.setAttribute("class", "form-control w-75 mx-auto mt-5");
	pwd2.setAttribute("placeholder", "Repita contraseña");
	document.getElementById("login").appendChild(pwd2);
}

function addNick(){
	var nick = document.createElement("INPUT");
	nick.setAttribute("id","nick");
	nick.setAttribute("name","nick")
	nick.setAttribute("type", "text");
	nick.setAttribute("class", "form-control w-75 mx-auto mt-5");
	nick.setAttribute("placeholder", "Nick");
	document.getElementById("login").appendChild(nick);
}

function changeNick(){
	document.getElementById("user-nick").disabled = false;
	document.getElementById("change-nick").remove();
}

function changePassword(){
	disableSubmit();
	document.getElementById("change-password").remove();
	document.getElementById("user-password1").hidden = false;
	document.getElementById("user-password1").required = true;
	document.getElementById("user-password2").hidden = false;
	document.getElementById("user-password2").required = true;
}

function moreInfo(){
	if(document.getElementById("info_button").attributes[1].value == "glyphicon glyphicon-chevron-down"){
		document.getElementById("basic_info").hidden = true;
		document.getElementById("extended_info").hidden = false;
		document.getElementById("info_button").attributes[1].value = "glyphicon glyphicon-chevron-up";
	} else{
		document.getElementById("basic_info").hidden = false;
		document.getElementById("extended_info").hidden = true;
		document.getElementById("info_button").attributes[1].value = "glyphicon glyphicon-chevron-down";
	}
}

function like(){
	if(document.getElementById("like-icon").attributes[1].value == "glyphicon glyphicon-heart-empty"){
		document.getElementById("like-icon").attributes[1].value = "glyphicon glyphicon-heart";
	}else{
		document.getElementById("like-icon").attributes[1].value = "glyphicon glyphicon-heart-empty";
	}
}

function disableSubmit(){
	document.getElementById("save-changes").disabled = true;

}

function checkPassword(){
	var pwd1 = document.getElementById("user-password1").value;
	var pwd2 = document.getElementById("user-password2").value;

	var msg1 = document.getElementById("pass-dis");
	var msg2 = document.getElementById("pass-range");
	var msg3 = document.getElementById("pass-length");

	msg1.hidden = true;
	msg2.hidden = true;
	msg3.hidden = true;

	if(pwd1 != pwd2){
		msg1.hidden = false;
		disableSubmit();
		return false;
	}
	if(pwd1.length<10){
		msg2.hidden = false;
		disableSubmit();
		return false;
	}
	if(!pwd1.match(/[A-Z]/g) || !pwd1.match(/[a-z]/g) || !pwd1.match(/[0-9]/g)){
		msg2.hidden = false;
		disableSubmit();
		return false;
	}

	return true;
}

function checkForm(){
	if(checkPassword()){
		document.getElementById("save-changes").disabled = false;
	}
}

function deleteImage(){
	document.getElementById("delete-img").value="true";
	document.getElementById("profile-img").src = "/static/img/user.png";
}