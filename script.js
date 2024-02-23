var date1=localStorage.getItem("date1");
			document.getElementById("date1").innerHTML = date1;
			var note1= localStorage.getItem("note1"); 
			document.getElementById("note1").innerHTML = note1;
			var chosen1= localStorage.getItem("information1");
			document.getElementById("information1").innerHTML = chosen1;
			var money1= localStorage.getItem("money1");
			document.getElementById("amount1").innerHTML = money1;
			var date2= localStorage.getItem("date2");
			document.getElementById("date2").innerHTML = date2;
			var note2= localStorage.getItem("note2"); 
			document.getElementById("note2").innerHTML = note2;
			var chosen2= localStorage.getItem("information2");
			document.getElementById("information2").innerHTML = chosen2;
			var money2= localStorage.getItem("money2");
			document.getElementById("amount2").innerHTML = money2;
			var date3= localStorage.getItem("date3");
			document.getElementById("date3").innerHTML = date3;
			var note3= localStorage.getItem("note3"); 
			document.getElementById("note3").innerHTML = note3;
			var chosen3= localStorage.getItem("information3");
			document.getElementById("information3").innerHTML = chosen3;
			var money4=localStorage.getItem("money3");
			document.getElementById("amount3").innerHTML = money3;
			var date4= localStorage.getItem("date4");
			document.getElementById("date4").innerHTML = date4;
			var note4= localStorage.getItem("note4"); 
			document.getElementById("note4").innerHTML = note4;
			var chosen4= localStorage.getItem("information4");
			document.getElementById("information4").innerHTML = chosen4;
			var money4= localStorage.getItem("money4");
			document.getElementById("amount4").innerHTML = money4;
			var date5= localStorage.getItem("date5");
			document.getElementById("date5").innerHTML = date5;
			var note5= localStorage.getItem("note5"); 
			document.getElementById("note5").innerHTML = note5;
			var chosen5= localStorage.getItem("information5");
			document.getElementById("information5").innerHTML = chosen5;
			var money5=localStorage.getItem("money5");
			document.getElementById("amount5").innerHTML = money5;
function control()
	{
		var money=document.input.money.value;
		var chosen=document.input.select.value;
		if(chosen=="Income")
		{
			//these is for balance
			var balance=localStorage.getItem("balance");
			if(balance=="undefined")
			{
			balance=0;
			}
			else if(balance=="NaN")
			{
				balance=0;
			}
			else
			{
				balance= +balance + +money;
			}
			localStorage.setItem("balance", balance);
			localStorage.getItem("balance");
			document.getElementById("balance").innerHTML = localStorage.getItem("balance");
			//total income
			var income=localStorage.getItem("income");
			if(income=="NaN")
			{
				income=0;
			}
			else
			{
				income= +income + +money;
			}
			localStorage.setItem("income", income);
			localStorage.getItem("income");
			document.getElementById("income").innerHTML = localStorage.getItem("income");
		}
		else
		{
			//these is for balance
			var balance=localStorage.getItem("balance");
			if(balance=="undefined")
			{
				balance=0;
			}
			else
			{
				balance= +balance - +money;
			}
			localStorage.setItem("balance", balance);
			localStorage.getItem("balance");
			document.getElementById("balance").innerHTML = localStorage.getItem("balance");
			//Total Expedichter
			var Expedichter=localStorage.getItem("Expedichter");
			if(Expedichter=="undefined")
			{
				Expedichter=0;
			}
			else if(Expedichter=="NaN")
			{
				Expedichter=0;
			}
			else
			{
				Expedichter= +Expedichter + +money;
			}
			localStorage.setItem("Expedichter", Expedichter);
			localStorage.getItem("Expedichter");
			document.getElementById("Expedichter").innerHTML = localStorage.getItem("Expedichter");
		}
	}
	function note()
		{
			const date= new Date();
			var chosen=document.input.select.value;
			var note=document.input.note.value;
			var money=document.input.money.value;
			var i=localStorage.getItem("i");
			i++;
			localStorage.setItem("i", i);
			if(i>5)
			{
				i=1;
				localStorage.setItem("i", i);
			}
			if(i==1)
			{
				localStorage.setItem("date1", date);
				var date1=localStorage.getItem("date1");
				document.getElementById("date1").innerHTML = date1;
				localStorage.setItem("note1",note);
				var note1= localStorage.getItem("note1"); 
				document.getElementById("note1").innerHTML = note1;
				localStorage.setItem("information1",chosen);
				var chosen1= localStorage.getItem("information1");
				document.getElementById("information1").innerHTML = chosen1;
				localStorage.setItem("money1",money);
				var money1= localStorage.getItem("money1");
				document.getElementById("amount1").innerHTML = money1;
			}
			else if(i==2)
			{
				localStorage.setItem("date2", date);
				var date2= localStorage.getItem("date2");
				document.getElementById("date2").innerHTML = date2;
				localStorage.setItem("note2",note);
				var note2= localStorage.getItem("note2"); 
				document.getElementById("note2").innerHTML = note2;
				localStorage.setItem("information2",chosen);
				var chosen2= localStorage.getItem("information2");
				document.getElementById("information2").innerHTML = chosen2;
				localStorage.setItem("money2",money);
				var money2= localStorage.getItem("money2");
				document.getElementById("amount2").innerHTML = money2;	
			}
			else if(i==3)
			{
				localStorage.setItem("date3", date);
				var date3= localStorage.getItem("date3");
				document.getElementById("date3").innerHTML = date3;
				localStorage.setItem("note3",note);
				var note3= localStorage.getItem("note3"); 
				document.getElementById("note3").innerHTML = note3;
				localStorage.setItem("information3",chosen);
				var chosen3= localStorage.getItem("information3");
				document.getElementById("information3").innerHTML = chosen3;
				localStorage.setItem("money3",money);
				var money3= localStorage.getItem("money3");
				document.getElementById("amount3").innerHTML = money3;	
			}
			else if(i==4)
			{
				localStorage.setItem("date4", date);
				var date4= localStorage.getItem("date4");
				document.getElementById("date4").innerHTML = date4;
				localStorage.setItem("note4",note);
				var note4= localStorage.getItem("note4"); 
				document.getElementById("note4").innerHTML = note4;
				localStorage.setItem("information4",chosen);
				var chosen4= localStorage.getItem("information4");
				document.getElementById("information4").innerHTML = chosen4;
				localStorage.setItem("money4",money);
				var money4= localStorage.getItem("money4");
				document.getElementById("amount4").innerHTML = money4;
			}
			else if(i==5)
			{
				localStorage.setItem("date5", date);
				var date5= localStorage.getItem("date5");
				document.getElementById("date5").innerHTML = date5;
				localStorage.setItem("note5",note);
				var note5= localStorage.getItem("note5"); 
				document.getElementById("note5").innerHTML = note5;
				localStorage.setItem("information5",chosen);
				var chosen5= localStorage.getItem("information5");
				document.getElementById("information5").innerHTML = chosen5;
				localStorage.setItem("money5",money);
				var money5=localStorage.getItem("money5");
				document.getElementById("amount5").innerHTML = money5;
			}
			var date1=localStorage.getItem("date1");
			document.getElementById("date1").innerHTML = date1;
			var note1= localStorage.getItem("note1"); 
			document.getElementById("note1").innerHTML = note1;
			var chosen1= localStorage.getItem("information1");
			document.getElementById("information1").innerHTML = chosen1;
			var money1= localStorage.getItem("money1");
			document.getElementById("amount1").innerHTML = money1;
			var date2= localStorage.getItem("date2");
			document.getElementById("date2").innerHTML = date2;
			var note2= localStorage.getItem("note2"); 
			document.getElementById("note2").innerHTML = note2;
			var chosen2= localStorage.getItem("information2");
			document.getElementById("information2").innerHTML = chosen2;
			var money2= localStorage.getItem("money2");
			document.getElementById("amount2").innerHTML = money2;
			var date3= localStorage.getItem("date3");
			document.getElementById("date3").innerHTML = date3;
			var note3= localStorage.getItem("note3"); 
			document.getElementById("note3").innerHTML = note3;
			var chosen3= localStorage.getItem("information3");
			document.getElementById("information3").innerHTML = chosen3;
			var money4=localStorage.getItem("money3");
			document.getElementById("amount3").innerHTML = money3;
			var date4= localStorage.getItem("date4");
			document.getElementById("date4").innerHTML = date4;
			var note4= localStorage.getItem("note4"); 
			document.getElementById("note4").innerHTML = note4;
			var chosen4= localStorage.getItem("information4");
			document.getElementById("information4").innerHTML = chosen4;
			var money4= localStorage.getItem("money4");
			document.getElementById("amount4").innerHTML = money4;
			var date5= localStorage.getItem("date5");
			document.getElementById("date5").innerHTML = date5;
			var note5= localStorage.getItem("note5"); 
			document.getElementById("note5").innerHTML = note5;
			var chosen5= localStorage.getItem("information5");
			document.getElementById("information5").innerHTML = chosen5;
			var money5=localStorage.getItem("money5");
			document.getElementById("amount5").innerHTML = money5;

		}
	function name()
	{
		var name;
		
		if(name=="undefined")
		{
			name=prompt("enter your name");
			document.write(name);
		}
	}