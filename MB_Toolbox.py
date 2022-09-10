import maya.cmds as cmds
import os.path
from os import listdir
import os


#path et outpath pour export
path = 'C:/Users/KOA049/Pictures/Maya_script_input/'
outpath = 'C:/Users/KOA049/Pictures/Maya_script_output/'

class MB_Window(object):

	#constructor
	def __init__(self):
		
		self.window = "ToolUI"
		self.title = "Marin Toolbox"
		self.size = (326, 300)
		self.bcolor = [202/255,255/255,255/255]
		self.buttonw = 103
		self.buttonh = 103
		self.FLh = 125
		self.FLw = 319
		self.framebgc = [141/255,179/255,179/255]
		self.rowbgc = [141/255,179/255,179/255]
		self.tabbgc = [101/255,128/255,128/255]
		
		# close old window is open
		if cmds.window(self.window, exists = True):
			cmds.deleteUI(self.window, window=True)
		
		#create new window
		self.window = cmds.window(self.window, title=self.title, widthHeight=self.size, s=False,rtf=True)
		
		#tab
		MainL = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, bgc=self.tabbgc, scr=False)

		#tab1 = VR
		Page1L = cmds.columnLayout(p=MainL)	
		
		GeneralL = cmds.frameLayout(label='General', cll=True, la='top', bv=False, p=Page1L, en=True,  w=self.FLw, bgc=self.framebgc)
		
		cmds.columnLayout(p=GeneralL)
		
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)], bgc=self.rowbgc )

		self.general1 = cmds.symbolButton(image='newfile.png', c="newscene()", ann='new file', bgc=self.bcolor)
		self.general2 = cmds.symbolButton(image='tassethd3d.png', c="assetshd3d()", ann='Traitement asset hd3d', bgc=self.bcolor)
		self.general3 = cmds.symbolButton(image='cleanall.png', c="cleanall()", ann='Freeze Transform et Del History', bgc=self.bcolor)		

		
		HD3DVRL = cmds.frameLayout(label='HD3DVR', cll=True, la='top', bv=False, p=Page1L, en=True,  w=self.FLw, bgc=self.framebgc)
		
		cmds.columnLayout(p=HD3DVRL)
		
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)], bgc=self.rowbgc )

		self.hd3dvr1 = cmds.symbolButton(image='pfurniture.png', c="FurnitureP()", ann='Furniture pivot', bgc=self.bcolor)
		self.hd3dvr2 = cmds.symbolButton(image='pceilling.png', c="ceilingP()", ann='Ceiling pivot', bgc=self.bcolor)
		self.hd3dvr3 = cmds.symbolButton(image='pobjectwall.png', c="ObjwallP()", ann='Objectwall pivot', bgc=self.bcolor)
		
		cmds.setParent( '..' )
		
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)], bgc=self.rowbgc )

		self.hd3dvr4 = cmds.symbolButton(image='pstairs.png', c="stairsP()", ann='Stairs pivot', bgc=self.bcolor)
		self.hd3dvr5 = cmds.symbolButton(image='emptyB.png', c="ObjectCenterP()", ann='', bgc=self.bcolor)
		self.hd3dvr6 = cmds.symbolButton(image='emptyB.png', c="ObjectCenterP()", ann='', bgc=self.bcolor)
		
		
		CSVListes = cmds.frameLayout(label='CSV / Listes', cll=True, la='top', bv=False, p=Page1L, en=True,  w=self.FLw, bgc=self.framebgc)
		
		cmds.columnLayout(p=CSVListes)
		
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)], bgc=self.rowbgc )

		self.csv1 = cmds.symbolButton(image='listfile.png', c="listFile()", ann='Create list at path', bgc=self.bcolor)
		self.csv2 = cmds.symbolButton(image='listfullpath.png', c="listFile()", ann='Create full path list at path', bgc=self.bcolor)	
		self.csv3 = cmds.symbolButton(image='emptyB.png',  ann='', bgc=self.bcolor)

		
		#tab2 = V-Escape
		Page2L = cmds.columnLayout(p=MainL)
		
		VEscL = cmds.frameLayout(label='V-Escape', cll=True, la='top', bv=False, p=Page2L, en=True,  w=self.FLw, bgc=self.framebgc)
				
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )

		self.vescape1 = cmds.symbolButton(image='emptyB.png', c="freezeT()", ann='Freeze Transform et Del History', bgc=self.bcolor)
		self.vescape2 = cmds.symbolButton(image='tassethd3d.png', c="traitementnm()", ann='', bgc=self.bcolor)
		self.vescape3 = cmds.symbolButton(image='emptyB.png', c="newscene()", ann='Create new scene', bgc=self.bcolor)
		
		
		#tab3 = HD3D
		
		Page3L = cmds.columnLayout(p=MainL)
		
		ExportL = cmds.frameLayout(label='Import / Export', cll=True, la='top', bv=False, p=Page3L, en=True,  w=self.FLw, bgc=self.framebgc)
		
		cmds.columnLayout(p=ExportL)
				
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )

		self.hd3d1 = cmds.symbolButton(image='fbx.png', c="ExpFBX()", ann='', bgc=self.bcolor)
		self.hd3d2 = cmds.symbolButton(image='obj.png', c="ObjToFbx()", ann='', bgc=self.bcolor)
		self.hd3d3 = cmds.symbolButton(image='objtofbx.png', c="Regennm()", ann='', bgc=self.bcolor)
		
		cmds.setParent( '..' )
		
		cmds.rowLayout( numberOfColumns=3, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )

		self.hd3d4 = cmds.symbolButton(image='fbxplus.png', c="CeilingP()", ann='Ceiling pivot', bgc=self.bcolor)
		self.hd3d5 = cmds.symbolButton(image='objplus.png', c="stairsP()", ann='Stairs pivot', bgc=self.bcolor)
		self.hd3d6 = cmds.symbolButton(image='objtofbxplus.png', c="ObjwallP()", ann='Objectwall pivot', bgc=self.bcolor)
		
		
		
		#tab4 = TeamTO
		Page4L = cmds.columnLayout(p=MainL)
		
		TeamtoBL = cmds.frameLayout(label='Process', cll=True, la='top', bv=False, p=Page4L, en=True,  w=self.FLw, bgc=self.framebgc)
				
		cmds.rowLayout( numberOfColumns=3, columnWidth3=(100,100,100), adjustableColumn=2, columnAlign=(1,'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )

		self.Teamtobl1 = cmds.symbolButton(image='emptyB.png', bgc=self.bcolor)
		self.Teamtobl2 = cmds.symbolButton(image='emptyB.png', bgc=self.bcolor)
		self.Teamtobl3 = cmds.symbolButton(image='emptyB.png', bgc=self.bcolor)		
		
		cmds.setParent( '..' )
		
		TeamtoDeciL = cmds.frameLayout(label='Opti',cll=True, la='top', bv=False, p=Page4L, h=150, w=self.FLw, bgc=self.framebgc)
		
		self.pourcentage = cmds.intSliderGrp(label='Pourcentage :',field=True)
		self.decimationBtn = cmds.button(label='Decimate', command = self.decimation, bgc=self.bcolor )
		self.smoothangle = cmds.intSliderGrp(label='Smooth Angle :',field=True)
		self.smoothAngleBtn = cmds.button(label='Smooth', command = self.smoothAngle, bgc=self.bcolor )
		
		

		cmds.tabLayout( MainL, edit=True, tabLabel=((Page1L, 'HD3DVR'), (Page2L, 'V-Escape'), (Page3L, 'HD3D'), (Page4L, 'TeamTo')) )

		#display new window
		cmds.showWindow()
		
		

		
		
	def decimation(self, *args):
		
		percentage = cmds.intSliderGrp(self.pourcentage, query=True, value=True)

		cmds.polyReduce(p=percentage, kqw=True, ver=1)
		
		
		
	def smoothAngle(self, *args):
		
		smoothA = cmds.intSliderGrp(self.smoothangle, query=True, value=True)

		cmds.polySetToFaceNormal( setUserNormal=False )
		cmds.polySoftEdge( a=smoothA, ch=True )
		
		#Reexport d'fbx 2020.1
def ExpFBX():
	ExportAndNormal(False)
	
	
#Reexport d'fbx et regen des normal    
def Regennm():
	ExportAndNormal(True)
    
def ExportAndNormal(normal: bool):

	extention = '*.fbx'
	smoothA = 50
	if (normal):
		nmregen = 1
	else:
		nmregen = 0

	for i, fichier in enumerate(cmds.getFileList( folder= path, filespec= extention )):

		cmds.file(path + fichier, i=True, type='FBX', ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, namespace=os.path.splitext(fichier)[ 0 ], options='fbx', pr=True, importFrameRate=True, importTimeRange='override')
		print('import : ' + fichier)


		if nmregen == 1:
			zzz = cmds.ls(g=True)
			print(zzz)
			if len(zzz)!= 1 :
				cmds.select( all=True, hi=True )
				#merge
				cmds.polyUnite(name=os.path.splitext(fichier)[ 0 ], cch=True, ch=True)
				
				cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
				cmds.delete(all=True, constructionHistory=True)
				
			#center
			cmds.select(all=True)
			
			objet = cmds.ls(sl=True,visible=True,transforms=True)[0]
			bbox = cmds.exactWorldBoundingBox(objet)
			
			AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[1] , bbox[2]+(abs(bbox[5]-bbox[2]))/2 ))
			
			for i, objet in enumerate(cmds.ls(sl=True,visible=True,transforms=True)):
				
				cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
				
				objetRP = cmds.xform(objet, q=True, ws=True, rp=True)
				myOffset = [x * -1 for x in objetRP]
				cmds.xform(objet, ws=True, t=myOffset)

				cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
				
				
				
			#final rename
			cmds.select( ado=True, hi=True )
			cmds.rename(os.path.splitext(fichier)[ 0 ], ignoreShape=True)
			
			#force lambert1
			cmds.select( all=True, hi=True )
			cmds.sets(forceElement='initialShadingGroup')
			
			#clear ch
			cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
			cmds.delete(all=True, constructionHistory=True)

	else:
		pass

	cmds.file( outpath + fichier, f=True, options='v=0', type='FBX export', pr=True, ea=True)
	print('export : '+ fichier)
	cmds.file( f=True, new=True )
	
	
#Reexport d'obj
def ExpOBJ():
	
	extention = '*.obj'


	for i, fichier in enumerate(cmds.getFileList( folder= path, filespec= extention )):

		cmds.file(path + fichier, i=True, type='OBJ', ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, namespace=os.path.splitext(fichier)[ 0 ], options='mo=1', pr=True, importFrameRate=True, importTimeRange='override')
		print('import : ' + fichier)


		cmds.file( outpath + fichier, f=True, options='groups=1;ptgroups=1;materials=1;smoothing=1;normals=1', type='OBJexport', pr=True, ea=True)
		print('export : '+ fichier)

		cmds.file( f=True, new=True )
	
	
	
	
	
	
#Pivot furniture
def FurnitureP():
	IsWall('furniture')
	
	
#Pivot object wall
def ObjwallP():
	IsWall('wall')
	
def ceilingP():
	IsWall('ceiling')
	
def ObjectCenterP():
	IsWall('center')
	
	
#freeze tranform + placement de pivot + placement a l'origine 0,0,0
def IsWall(WallP: str):
	
	
	#cmds.select(all=True)
	
	#cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	
	
	objet = cmds.ls(sl=True,visible=True,transforms=True)[0]
	bbox = cmds.exactWorldBoundingBox(objet)
	#print (objet)
	#print (bbox)
	#centerbbox = ((abs(bbox[3]-bbox[0]))/2 , (abs(bbox[4]-bbox[1]))/2 , (abs(bbox[5]-bbox[2]))/2)
	#print(centerbbox[0]*-1,centerbbox[1]*-1,centerbbox[2]*-1)
	
	if WallP=='furniture':
		AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[1] , bbox[2]+(abs(bbox[5]-bbox[2]))/2 ))
	if WallP=='wall':
		AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[1]+(abs(bbox[4]-bbox[1]))/2 , bbox[2] ))
	if WallP=='ceiling':
		AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[4] , bbox[2]+(abs(bbox[5]-bbox[2]))/2 ))
	if WallP=='center':
		AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[1]+(abs(bbox[4]-bbox[1]))/2 , bbox[2]+(abs(bbox[5]-bbox[2]))/2 ))
		cmds.move(0,0,0, rpr=True)

	#for i, objet in enumerate(cmds.ls(sl=True,visible=True,transforms=True)):
		
	#	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
		
	#	objetRP = cmds.xform(objet, q=True, ws=True, rp=True)
	#	myOffset = [x * -1 for x in objetRP]
	#	cmds.xform(objet, ws=True, t=myOffset)
	#	print(objet)
	#	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)



def traitementnm():
	#scale 0.01 peut importe le pivot
	sel = cmds.ls(transforms=True, visible=True)
	print (sel)
	cmds.select(sel)
	
	cmds.group( sel, n='scale_grp')
	
	cmds.xform(piv=(0,0,0))
	
	cmds.scale(0.01,0.01,0.01)
	cmds.viewFit()
	
	cmds.parent( sel, w=True )
	cmds.parent( 'scale_grp', removeObject=True )
	
	cmds.select(sel)
	cmds.makeIdentity( apply=True )


def stairsP():
	#Step
	if cmds.objExists('step'):
		cmds.select('step')
		
		step = cmds.ls(sl=True)
		
		bboxstep = cmds.exactWorldBoundingBox(step)
		
		stepx =(abs(bboxstep[3]-bboxstep[0]))/2
		
		cmds.xform(piv=( bboxstep[0]+ stepx , bboxstep[4] , bboxstep[5] ))
		
		cmds.move(0,0,0, rpr=True)
		cmds.makeIdentity( apply=True )
		cmds.move(0,18,0,)
		cmds.makeIdentity( apply=True )
		cmds.xform(piv=(0,0,0))
	else:
		cmds.error("TY EST FADA IL EST OU LE step")
		
	#Landing_L
	if cmds.objExists('landing_L'):
		cmds.select('landing_L')
		cmds.makeIdentity( apply=True )
		landingl = cmds.ls(sl=True)
		
		bboxlandingl = cmds.exactWorldBoundingBox(landingl)
			
		print(stepx)
			
		cmds.xform(piv=( bboxlandingl[0]+stepx , bboxlandingl[4] , bboxlandingl[5] ))
		cmds.move(0,0,0, rpr=True)
		cmds.makeIdentity( apply=True )
		cmds.move(0,18,0,)
		cmds.makeIdentity( apply=True )
		cmds.xform(piv=(0,0,0))
	else:
		cmds.error("TY EST FADA IL EST OU LE landing_L")
	
	#Landing_U
	if cmds.objExists('landing_U'):
		cmds.select('landing_U')
		cmds.makeIdentity( apply=True )
		landingu = cmds.ls(sl=True)
		
		bboxlandingu = cmds.exactWorldBoundingBox(landingu)
		
		print(stepx)
		
		cmds.xform(piv=( bboxlandingu[0]+stepx , bboxlandingu[4] , bboxlandingu[5] ))
		cmds.move(0,0,0, rpr=True)
		cmds.makeIdentity( apply=True )
		cmds.move(0,18,0,)
		cmds.makeIdentity( apply=True )
		cmds.xform(piv=(0,0,0))
	else:
		cmds.error("TY EST FADA IL EST OU LE landing_U")
		
	#Body_L
	if cmds.objExists('body_L'):
		cmds.select('body_L')
		cmds.makeIdentity( apply=True )
		bodyl = cmds.ls(sl=True)
		
		
		bboxbodyl = cmds.exactWorldBoundingBox(bodyl)
		print(bboxbodyl)
		print(bboxlandingl)
		print(abs(bboxlandingl[3]-bboxlandingl[0]))
		
		cmds.xform(piv=( bboxbodyl[0]+stepx , bboxbodyl[4] , bboxbodyl[5] ))
		cmds.move(0,0,0, rpr=True)
		cmds.makeIdentity( apply=True )
		cmds.move(0,18,0,)
		cmds.makeIdentity( apply=True )
		cmds.xform(piv=(0,0,0))
	else:
		cmds.error("TY EST FADA IL EST OU LE body_L")
		
	#Body_U
	if cmds.objExists('body_U'):
		cmds.select('body_U')
		cmds.makeIdentity( apply=True )
		bodyu = cmds.ls(sl=True)
		
		
		bboxbodyu = cmds.exactWorldBoundingBox(bodyu)
		
		cmds.xform(piv=( bboxbodyu[0]+stepx , bboxbodyu[4] , bboxbodyu[5] ))
		cmds.move(0,0,0, rpr=True)
		cmds.makeIdentity( apply=True )
		cmds.move(0,18,0,)
		cmds.makeIdentity( apply=True )
		cmds.xform(piv=(0,0,0))
		
		cmds.xform(piv=( abs(bboxlandingu[3]-bboxlandingu[0])/2 , bboxbodyu[4] , bboxbodyu[5] ))
	else:
		cmds.error("TY EST FADA IL EST OU LE body_U")
		
	
def newscene():
	cmds.file( f=True, new=True )	
		
def freezeT():
	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	cmds.delete(all=True, constructionHistory=True)
	
def scale100():
	cmds.scale(100,100,100)
	cmds.viewFit()
	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	cmds.delete(all=True, constructionHistory=True)
	
def scale001():
	cmds.scale(0.01,0.01,0.01)
	cmds.viewFit()
	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	cmds.delete(all=True, constructionHistory=True)

def cleanall():
	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	cmds.delete(all=True, constructionHistory=True)
	mel.eval("cleanUpScene 3")
	
def assetshd3d():
	#scale 100 peut importe le pivot
	sel = cmds.ls(transforms=True, visible=True)
	print (sel)
	cmds.select(sel)
	
	cmds.group( sel, n='scale_grp')
	
	cmds.xform(piv=(0,0,0))
	
	cmds.scale(100,100,100)
	cmds.viewFit()
	
	cmds.parent( sel, w=True )
	cmds.parent( 'scale_grp', removeObject=True )
	
	cmds.select(sel)
	cmds.makeIdentity( apply=True )
	
	#apply lambert 1 et clean
	cmds.sets(forceElement='initialShadingGroup')
	
	cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
	cmds.delete(all=True, constructionHistory=True)
	mel.eval("cleanUpScene 3")
	
	
#Obj vers fbx + manip
def ObjToFbx():
	
	extention = '*.obj'


	for i, fichier in enumerate(cmds.getFileList( folder= path, filespec= extention )):

		cmds.file(path + fichier, i=True, type='OBJ', ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, namespace=os.path.splitext(fichier)[ 0 ], options='mo=1', pr=True, importFrameRate=True, importTimeRange='override')
		print('import : ' + fichier)

		zzz = cmds.ls(g=True)
		print(zzz)
		if len(zzz)!= 1 :
			cmds.select( all=True, hi=True )
			#merge
			cmds.polyUnite(name=os.path.splitext(fichier)[ 0 ], cch=True, ch=True)
			
			cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
			cmds.delete(all=True, constructionHistory=True)
			
		#center
		cmds.select(all=True)
		
		objet = cmds.ls(sl=True,visible=True,transforms=True)[0]
		bbox = cmds.exactWorldBoundingBox(objet)
		
		AssetP = cmds.xform(piv=(bbox[0]+(abs(bbox[3]-bbox[0]))/2  , bbox[1] , bbox[2]+(abs(bbox[5]-bbox[2]))/2 ))
		
		for i, objet in enumerate(cmds.ls(sl=True,visible=True,transforms=True)):
			
			cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
			
			objetRP = cmds.xform(objet, q=True, ws=True, rp=True)
			myOffset = [x * -1 for x in objetRP]
			cmds.xform(objet, ws=True, t=myOffset)
			cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
		
		
		
		#clear namespace
		
		# Set root namespace
		cmds.namespace(setNamespace=':')
		
		# Collect all namespaces except for the Maya built ins.
		all_namespaces = [x for x in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True) if x != "UI" and x != "shared"]
		
		if all_namespaces:
			# Sort by hierarchy, deepest first.
			all_namespaces.sort(key=len, reverse=True)
			for namespace in all_namespaces:
				# When a deep namespace is removed, it also removes the root. So check here to see if these still exist.
				if cmds.namespace(exists=namespace) is True:
					cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=True)
		
		
		
		#final rename
		cmds.select( ado=True, hi=True )
		cmds.rename(os.path.splitext(fichier)[ 0 ], ignoreShape=True)
		
		#force lambert1
		cmds.select( all=True, hi=True )
		cmds.sets(forceElement='initialShadingGroup')
		
		#clear ch
		cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
		cmds.delete(all=True, constructionHistory=True)
		mel.eval("cleanUpScene 3")

		cmds.file( outpath + fichier, f=True, options='v=0', type='FBX export', pr=True, ea=True)
		print('export : '+ fichier)

		cmds.file( f=True, new=True )
	

def listF():

	directory_path = 'C:/Users/KOA049/Documents/1_Vrenamed/alb'
	txt_path = 'C:/Users/KOA049/Pictures/Maya_script_output/liste.txt'

	with open(txt_path, 'w+') as fichier:
		onlyfiles = [os.path.splitext(f)[ 0 ] for f in listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
		sorted(onlyfiles)
		fichier.write('\n'.join(onlyfiles))
    
	print('TADAAAAAA')
	
	


def addPathToCsv(path,fichier):
        for root, directories, files in os.walk(path, topdown=False):
           # if root in ignorePath:
           #     continue
               
            for name in files:
                if name.endswith('.png') and "_nm" not in name.lower():
                    #fichier.write(os.path.join(root, name) + '\n')
                    fichier.write(os.path.splitext(name)[ 0 ]+'\n')
                    print(root)

def listFullPath():
	
	path = 'D:/Graphs/Assets/PREFAB_TRAITEMENT'
	path2 = 'D:/Graphs/Assets/Resources/Furnitures/PREFAB_HD3D'
	
	paths = [path,path2]
	
	ignore1 = 'D:/Graphs/Assets/PREFAB_TRAITEMENT\Arches'
	ignore2 = 'D:/Graphs/Assets/PREFAB_TRAITEMENT\Barrieres'
	ignore3 = 'D:/Graphs/Assets/PREFAB_TRAITEMENT\Colonnes'
	
	ignorePath = [ignore1, ignore2, ignore3]
	
	with open(txt_path, 'w+') as fichier:
	
		for path in paths:
			addPathToCsv(path,fichier)
	
	
	print('TADAAAAAA')

def listFile():
	
	txt_path = 'C:/Users/HOLEAU/Downloads/tex_hd3d/liste.txt'
	
	path = 'C:/Users/HOLEAU/Downloads/tex_hd3d/All_clean'
#	path2 = 'D:/Graphs/Assets/Resources/Furnitures/PREFAB_HD3D'
	
	paths = [path]
	
	ignore1 = ''
#	ignore2 = 'D:/Graphs/Assets/PREFAB_TRAITEMENT\Barrieres'
#	ignore3 = 'D:/Graphs/Assets/PREFAB_TRAITEMENT\Colonnes'
	
	ignorePath = [ignore1]
	
	with open(txt_path, 'w+') as fichier:
	
		for path in paths:
			addPathToCsv(path,fichier)
	
	
	print('VOILAAAAA')

myWindow = MB_Window()
