from django.shortcuts import render

# Create your views here.

def  metcal(whidth,heigth):
	return (float(whidth)+float(heigth))*2
	
def steclow(w):
	return float(w)-0.070
def stecloh(h):
	return float(h)-0.070
def sum(a,b,c):
	return float(((a*b)*2000)+(c*1200))
	
def calcmat(request):
	if request.method=='POST':
		whidth=request.POST['whidth']
		heigth=request.POST['heigth']

		if 'calc' in request.POST:
			resalt=metcal(whidth,heigth)
			steclopackW=steclow(whidth)
			steclopackH=stecloh(heigth)
			itog=sum(steclopackW,steclopackH,resalt)
			return render(request,'calcmaterial/calcmaterial.html',{'resalt':resalt,'steclopackW':steclopackW,'steclopackH':steclopackH,'itog':itog})
	return render(request,'calcmaterial/calcmaterial.html')		
	