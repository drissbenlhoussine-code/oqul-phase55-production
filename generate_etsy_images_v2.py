#!/usr/bin/env python3
"""Etsy Product Images v2 — professional: gradients, shadows, doc mockups, device mockups"""
import os, zipfile, traceback
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = "/home/user/oqul-phase55-production/etsy-images-v2"
os.makedirs(OUT, exist_ok=True)
SIZE = 2000

# ── Fonts ─────────────────────────────────────────────────────
_SERIF  = ["/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf",
           "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
_BOLD   = ["/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
           "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf"]
_REG    = ["/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"]

_fcache = {}
def F(family, size):
    key = (family, size)
    if key in _fcache: return _fcache[key]
    paths = _SERIF if family=='serif' else (_BOLD if family=='bold' else _REG)
    for p in paths:
        try:
            f = ImageFont.truetype(p, int(size)); _fcache[key]=f; return f
        except: pass
    f = ImageFont.load_default(); _fcache[key]=f; return f

# ── Color helpers ─────────────────────────────────────────────
def h2r(h):
    h=h.lstrip('#'); return (int(h[0:2],16),int(h[2:4],16),int(h[4:6],16))

def r2h(t): return '#{:02x}{:02x}{:02x}'.format(*t)

def mix(c1,c2,t):
    if isinstance(c1,str): c1=h2r(c1)
    if isinstance(c2,str): c2=h2r(c2)
    return tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))

def lighten(c, f=0.35):
    if isinstance(c,str): c=h2r(c)
    return tuple(int(v+(255-v)*f) for v in c)

def darken(c, f=0.3):
    if isinstance(c,str): c=h2r(c)
    return tuple(int(v*(1-f)) for v in c)

# ── Drawing primitives ────────────────────────────────────────
def grad_v(draw, x1,y1,x2,y2, c1,c2):
    if isinstance(c1,str): c1=h2r(c1)
    if isinstance(c2,str): c2=h2r(c2)
    n=int(y2-y1)
    if n<=0: return
    for i in range(n):
        t=i/n; c=mix(c1,c2,t)
        draw.line([(int(x1),int(y1+i)),(int(x2),int(y1+i))],fill=c)

def grad_h(draw, x1,y1,x2,y2, c1,c2):
    if isinstance(c1,str): c1=h2r(c1)
    if isinstance(c2,str): c2=h2r(c2)
    n=int(x2-x1)
    if n<=0: return
    for i in range(n):
        t=i/n; c=mix(c1,c2,t)
        draw.line([(int(x1+i),int(y1)),(int(x1+i),int(y2))],fill=c)

def shadow(img, bbox, r=18, off=10, blur=18, a=75):
    sh=Image.new('RGBA',img.size,(0,0,0,0))
    sd=ImageDraw.Draw(sh)
    x1,y1,x2,y2=[int(v) for v in bbox]
    sd.rounded_rectangle([x1+off,y1+off,x2+off,y2+off],radius=r,fill=(0,0,0,a))
    sh=sh.filter(ImageFilter.GaussianBlur(blur))
    out=Image.alpha_composite(img.convert('RGBA'),sh)
    return out.convert('RGB')

def dots(draw, x1,y1,x2,y2, col, sp=58, r=4):
    if isinstance(col,str): col=h2r(col)
    for y in range(int(y1),int(y2),sp):
        for x in range(int(x1),int(x2),sp):
            draw.ellipse([x-r,y-r,x+r,y+r],fill=col)

def tcx(draw, text, cx, cy, font, fill=(255,255,255)):
    bb=draw.textbbox((0,0),text,font=font)
    w,h=bb[2]-bb[0],bb[3]-bb[1]
    draw.text((cx-w//2,cy-h//2),text,font=font,fill=fill)

def rr(draw, box, radius=12, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

# ── Document mockups ──────────────────────────────────────────
def mock_excel(img, x,y,w,h, pri,acc):
    draw=ImageDraw.Draw(img)
    rr(draw,[x,y,x+w,y+h],10,fill=(255,255,255))
    # header bar
    draw.rectangle([x,y,x+w,y+28],fill=(33,115,70))
    rr(draw,[x,y,x+w,y+28],10,fill=(33,115,70))
    draw.rectangle([x,y+18,x+w,y+28],fill=(33,115,70))
    fb=F('bold',12); fs=F('reg',9)
    draw.text((x+6,y+7),"EXCEL",font=fb,fill=(255,255,255))
    # col headers
    cols=5; cw=w//cols
    for i,lbl in enumerate(['A','B','C','D','E']):
        cx2=x+i*cw
        draw.rectangle([cx2,y+28,cx2+cw,y+42],fill=(217,234,211))
        draw.line([cx2,y+28,cx2,y+h-4],fill=(198,224,180))
        tcx(draw,lbl,cx2+cw//2,y+35,fs,(80,80,80))
    # data rows
    acc_r=h2r(acc); pri_r=h2r(pri)
    rh=max(14,(h-50)//7)
    for ri in range(7):
        ry=y+42+ri*rh
        if ry+rh>y+h-2: break
        bg=(255,255,255) if ri%2==0 else (240,248,240)
        draw.rectangle([x,ry,x+w,ry+rh],fill=bg)
        draw.line([x,ry+rh,x+w,ry+rh],fill=(198,224,180))
        # colored bar in col A
        bc=acc_r if ri%3==0 else (pri_r if ri%3==1 else (70,130,180))
        bw2=min(cw-6,55)
        draw.rectangle([x+3,ry+2,x+3+bw2,ry+rh-2],fill=bc)
        # gray lines in other cols
        for ci in range(1,5):
            lw2=int((cw-6)*(0.85-ci*0.08))
            draw.rectangle([x+ci*cw+3,ry+4,x+ci*cw+3+lw2,ry+rh-4],fill=(190,210,190))
    rr(draw,[x,y,x+w,y+h],10,outline=(170,200,170))
    return img

def mock_word(img, x,y,w,h, pri,acc):
    draw=ImageDraw.Draw(img)
    rr(draw,[x,y,x+w,y+h],10,fill=(255,255,255))
    rr(draw,[x,y,x+w,y+26],10,fill=(43,87,154))
    draw.rectangle([x,y+16,x+w,y+26],fill=(43,87,154))
    fb=F('bold',12)
    draw.text((x+6,y+7),"WORD",font=fb,fill=(255,255,255))
    pad=14
    # title block
    draw.rectangle([x+pad,y+34,x+w-pad,y+56],fill=h2r(pri))
    tw2=int((w-2*pad)*0.65)
    draw.rectangle([x+pad+4,y+37,x+pad+4+tw2,y+50],fill=h2r(acc))
    draw.line([x+pad,y+62,x+w-pad,y+62],fill=(210,210,210),width=2)
    # text lines
    lhs=[70,82,94,108,120,132,148,160,172]
    lws=[0.88,0.65,0.80,0.55,0.75,0.60,0.82,0.50,0.70]
    for ly_off,lw2 in zip(lhs,lws):
        if y+ly_off>y+h-16: break
        pw2=int((w-2*pad)*lw2)
        col=(90,90,90) if lw2>0.7 else (140,140,140)
        rr(draw,[x+pad,y+ly_off,x+pad+pw2,y+ly_off+6],3,fill=col)
    # bullet points
    for bi in range(3):
        by2=y+182+bi*20
        if by2>y+h-12: break
        draw.ellipse([x+pad,by2+2,x+pad+8,by2+10],fill=h2r(acc))
        bw2=int((w-2*pad-14)*0.7)
        rr(draw,[x+pad+14,by2+3,x+pad+14+bw2,by2+9],2,fill=(150,150,150))
    rr(draw,[x,y,x+w,y+h],10,outline=(190,190,190))
    return img

def mock_pdf(img, x,y,w,h, pri,acc):
    draw=ImageDraw.Draw(img)
    # page shadow
    draw.rectangle([x+3,y+3,x+w+3,y+h+3],fill=(200,200,200))
    rr(draw,[x,y,x+w,y+h],10,fill=(255,255,255))
    rr(draw,[x,y,x+w,y+26],10,fill=(190,30,45))
    draw.rectangle([x,y+16,x+w,y+26],fill=(190,30,45))
    fb=F('bold',12)
    draw.text((x+6,y+7),"PDF",font=fb,fill=(255,255,255))
    pad=10; sec_h=max(20,(h-38)//5)
    pri_r=h2r(pri); acc_r=h2r(acc)
    for i in range(5):
        sy=y+32+i*(sec_h+4)
        if sy+sec_h>y+h-4: break
        bc=pri_r if i%2==0 else acc_r
        rr(draw,[x+pad,sy,x+pad+sec_h-2,sy+sec_h-2],4,fill=bc)
        nf=F('bold',min(13,sec_h-5))
        tcx(draw,str(i+1),x+pad+(sec_h-2)//2,sy+(sec_h-2)//2,nf,(255,255,255))
        rr(draw,[x+pad+sec_h+2,sy,x+w-pad,sy+sec_h-2],4,fill=(248,248,248),outline=(220,220,220))
        lw2=int((w-2*pad-sec_h-6)*0.78)
        rr(draw,[x+pad+sec_h+8,sy+4,x+pad+sec_h+8+lw2,sy+10],2,fill=(160,160,160))
        lw3=int((w-2*pad-sec_h-6)*0.52)
        rr(draw,[x+pad+sec_h+8,sy+14,x+pad+sec_h+8+lw3,sy+sec_h-6],2,fill=(190,190,190))
    rr(draw,[x,y,x+w,y+h],10,outline=(190,190,190))
    return img

def mock_pptx(img, x,y,w,h, pri,acc):
    draw=ImageDraw.Draw(img)
    rr(draw,[x,y,x+w,y+h],10,fill=h2r(pri))
    grad_v(draw,x,y,x+w,y+h,pri,r2h(lighten(pri,0.3)))
    draw.rectangle([x,y,x+w,y+22],fill=h2r(acc))
    rr(draw,[x,y,x+w,y+22],10,fill=h2r(acc))
    draw.rectangle([x,y+12,x+w,y+22],fill=h2r(acc))
    fb=F('bold',12)
    draw.text((x+6,y+6),"PPTX",font=fb,fill=(255,255,255))
    # title area
    tw2=w-20
    rr(draw,[x+10,y+28,x+10+tw2,y+50],5,fill=lighten(pri,0.25))
    rr(draw,[x+10,y+30,x+10+int(tw2*0.65),y+40],3,fill=(255,255,255))
    rr(draw,[x+10,y+42,x+10+int(tw2*0.45),y+48],3,fill=lighten(acc,0.4))
    # bar chart
    bars=[0.38,0.72,0.55,0.90,0.62]
    bw2=max(8,(w-24)//len(bars)-6)
    cb=h-70
    for i,v in enumerate(bars):
        bx2=x+12+i*(bw2+6)
        bh2=int((cb-30)*v)
        col=h2r(acc) if i==3 else lighten(pri,0.5)
        rr(draw,[bx2,y+cb-bh2,bx2+bw2,y+cb],3,fill=col)
    draw.line([x+10,y+cb+2,x+w-10,y+cb+2],fill=lighten(pri,0.5))
    # slide thumbnails
    for ti in range(3):
        tx2=x+w-16; ty2=y+28+ti*26
        rr(draw,[tx2,ty2,tx2+10,ty2+18],2,fill=lighten(pri,0.5))
    rr(draw,[x,y,x+w,y+h],10,outline=(180,180,180))
    return img

def mock_csv(img, x,y,w,h, pri,acc):
    draw=ImageDraw.Draw(img)
    rr(draw,[x,y,x+w,y+h],10,fill=(255,255,255))
    teal=(0,128,128)
    rr(draw,[x,y,x+w,y+26],10,fill=teal)
    draw.rectangle([x,y+16,x+w,y+26],fill=teal)
    fb=F('bold',12)
    draw.text((x+6,y+7),"CSV",font=fb,fill=(255,255,255))
    cols=4; cw2=(w-4)//cols; rh2=max(13,(h-42)//7)
    draw.rectangle([x+2,y+26,x+w-2,y+26+rh2],fill=(230,255,255))
    for ci in range(cols):
        cx2=x+2+ci*cw2
        cw3=min(cw2-6,38)
        rr(draw,[cx2+3,y+29,cx2+3+cw3,y+26+rh2-3],2,fill=teal)
        draw.line([cx2,y+26,cx2,y+h-4],fill=(190,230,230))
    sc=[(40,167,69),(255,193,7),(220,53,69),(0,123,255),(40,167,69),(255,193,7)]
    for ri in range(6):
        ry=y+26+rh2*(ri+1)
        if ry+rh2>y+h-3: break
        bg=(248,252,252) if ri%2==0 else (255,255,255)
        draw.rectangle([x+2,ry,x+w-2,ry+rh2],fill=bg)
        draw.line([x+2,ry+rh2,x+w-2,ry+rh2],fill=(200,230,230))
        draw.rectangle([x+4,ry+3,x+4+28,ry+rh2-3],fill=sc[ri%len(sc)])
        for ci in range(1,cols):
            dw2=int((cw2-8)*(0.75-ci*0.08))
            rr(draw,[x+2+ci*cw2+3,ry+4,x+2+ci*cw2+3+dw2,ry+rh2-4],2,fill=(190,215,215))
    rr(draw,[x,y,x+w,y+h],10,outline=(180,220,220))
    return img

# ── Device mockups ────────────────────────────────────────────
def laptop(img, cx,cy, sw, pri,acc, line1,line2,files):
    sh=int(sw*0.64); bz=int(sw*0.04)
    lx1=cx-sw//2; ly1=cy-sh//2; lx2=cx+sw//2; ly2=cy+sh//2
    img=shadow(img,[lx1,ly1,lx2,ly2],r=16,off=14,blur=22,a=80)
    draw=ImageDraw.Draw(img)
    rr(draw,[lx1,ly1,lx2,ly2],14,fill=(28,28,32))
    # screen
    sx1=lx1+bz; sy1=ly1+bz; sx2=lx2-bz; sy2=ly2-bz
    sw2=sx2-sx1; sh2=sy2-sy1
    draw.rectangle([sx1,sy1,sx2,sy2],fill=h2r(pri))
    grad_v(draw,sx1,sy1,sx2,sy2,pri,r2h(lighten(pri,0.3)))
    # screen content
    f1=F('bold',max(14,sw2//13)); f2=F('reg',max(10,sw2//20)); f3=F('bold',max(11,sw2//18))
    bb=draw.textbbox((0,0),line1,font=f1)
    draw.text((cx-(bb[2]-bb[0])//2,sy1+sh2//5),line1,font=f1,fill=(255,255,255))
    bb2=draw.textbbox((0,0),line2,font=f2)
    draw.text((cx-(bb2[2]-bb2[0])//2,sy1+sh2//5+f1.size+6),line2,font=f2,fill=lighten(acc,0.5))
    badge=f"{files}+ FILES"
    bb3=draw.textbbox((0,0),badge,font=f3)
    bw2=bb3[2]-bb3[0]
    bx1=cx-bw2//2-14; by1=sy1+sh2*2//3
    rr(draw,[bx1,by1,bx1+bw2+28,by1+f3.size+12],8,fill=h2r(acc))
    draw.text((bx1+14,by1+6),badge,font=f3,fill=h2r(pri))
    # webcam
    draw.ellipse([cx-4,ly1+5,cx+4,ly1+11],fill=(50,50,55))
    # keyboard base
    bw3=int(sw*1.15); bh2=int(sh*0.14)
    bx1=cx-bw3//2; by1=ly2; bx2=cx+bw3//2; by2=ly2+bh2
    rr(draw,[bx1,by1,bx2,by2],7,fill=(38,38,42))
    # keys
    kc=12; kr=4; kx0=bx1+int(bw3*0.06); ky0=by1+int(bh2*0.15)
    kw2=int(bw3*0.85)//kc-3; kh2=max(4,int(bh2*0.17))
    for r2 in range(kr):
        for c2 in range(kc):
            kx2=kx0+c2*(kw2+3); ky2=ky0+r2*(kh2+3)
            if kx2+kw2>bx2-5 or ky2+kh2>by2-3: continue
            rr(draw,[kx2,ky2,kx2+kw2,ky2+kh2],1,fill=(52,52,57))
    tp=int(bw3*0.22); th=int(bh2*0.55)
    rr(draw,[cx-tp//2,by1+int(bh2*0.3),cx+tp//2,by1+int(bh2*0.3)+th],5,fill=(48,48,52))
    draw.rounded_rectangle([cx-int(bw3*0.35),by2,cx+int(bw3*0.35),by2+5],radius=2,fill=(55,55,60))
    return img

def phone(img, cx,cy, pw, pri,acc):
    ph=int(pw*2.1); cr=int(pw*0.13)
    px1=cx-pw//2; py1=cy-ph//2; px2=cx+pw//2; py2=cy+ph//2
    img=shadow(img,[px1,py1,px2,py2],r=cr,off=9,blur=18,a=75)
    draw=ImageDraw.Draw(img)
    rr(draw,[px1,py1,px2,py2],cr,fill=(18,18,22))
    sp=int(pw*0.05)
    sx1=px1+sp; sy1=py1+int(ph*0.07); sx2=px2-sp; sy2=py2-int(ph*0.07)
    sw2=sx2-sx1; sh2=sy2-sy1
    draw.rectangle([sx1,sy1,sx2,sy2],fill=h2r(pri))
    grad_v(draw,sx1,sy1,sx2,sy2,r2h(lighten(pri,0.15)),pri)
    # notch
    nw=int(pw*0.35); nh=int(ph*0.035)
    rr(draw,[cx-nw//2,sy1,cx+nw//2,sy1+nh],nh//2,fill=(18,18,22))
    # mini chart
    ct=sy1+int(sh2*0.22); cb2=sy2-int(sh2*0.12)
    cl=sx1+int(sw2*0.1); cr2=sx2-int(sw2*0.1)
    ch2=cb2-ct; cw2=cr2-cl
    bars=[0.45,0.75,0.55,0.88,0.65]
    bw2=cw2//(len(bars)*2)
    for i,v in enumerate(bars):
        bx2=cl+i*(bw2*2); bh2=int(ch2*v)
        col=h2r(acc) if i==3 else lighten(pri,0.6)
        rr(draw,[bx2,cb2-bh2,bx2+bw2,cb2],3,fill=col)
    draw.line([cl,cb2+2,cr2,cb2+2],fill=lighten(pri,0.5))
    # home bar
    hw=int(pw*0.32)
    rr(draw,[cx-hw//2,py2-int(ph*0.04),cx+hw//2,py2-int(ph*0.02)],3,fill=(75,75,80))
    return img

# ── Products ──────────────────────────────────────────────────
PRODUCTS=[
 {"id":"01","name":"Mortgage Broker","title":"Mortgage Broker Business Kit","sub":"Complete Client & Operations System","pri":"#0A2342","acc":"#C9A84C","files":47,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Client Intake Forms","Loan Tracker","Rate Sheets","Closing Checklist","CRM Templates","Email Scripts","Marketing Plan","Business Planner"],"pillars":["Lead Management","Client Onboarding","Loan Processing","Closing Process","Business Growth"],"before":["Scattered client notes","Missing deadlines","No follow-up system","Manual tracking"],"after":["Organized CRM system","Automated reminders","Professional scripts","One-click reports"],"benefit":"Close More Deals"},
 {"id":"02","name":"Recruiting Agency","title":"Recruiting Agency Business Kit","sub":"Talent Acquisition & HR System","pri":"#2D1B69","acc":"#FF6B35","files":52,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Candidate Pipeline","Interview Scorecard","Job Descriptions","Offer Letter Kit","Client Portal","Revenue Tracker","SLA Templates","Process Guide"],"pillars":["Candidate Sourcing","Screening Process","Client Management","Offer Negotiation","Business Scaling"],"before":["Lost candidate info","No screening system","Missed placements","Disorganized pipeline"],"after":["Full ATS tracker","Structured interviews","Client dashboard","Automated workflows"],"benefit":"Place Candidates Faster"},
 {"id":"03","name":"Bookkeeping Business","title":"Bookkeeping Business Starter Kit","sub":"Client Accounting & Finance System","pri":"#1A4D2E","acc":"#D4AC0D","files":45,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Chart of Accounts","Client Onboarding","Invoice Templates","Expense Tracker","Monthly Reports","Tax Prep Checklist","Proposal Templates","Service Agreement"],"pillars":["Service Packages","Client Onboarding","Monthly Workflow","Report Delivery","Business Growth"],"before":["No pricing structure","Informal agreements","Manual calculations","No client process"],"after":["Clear service tiers","Professional contracts","Automated reports","Systematic workflow"],"benefit":"Land More Clients"},
 {"id":"04","name":"Real Estate Agent","title":"Real Estate Agent Business Kit","sub":"Client & Property Management System","pri":"#2C3E50","acc":"#E67E22","files":49,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Buyer/Seller CRM","Open House Kit","Listing Checklist","Commission Tracker","Showing Feedback","Marketing Templates","Closing Packet","Annual Business Plan"],"pillars":["Lead Generation","Buyer Journey","Listing Process","Negotiation","Closing & Referrals"],"before":["No lead tracking","Missed follow-ups","Manual paperwork","Inconsistent process"],"after":["Full CRM system","Automated follow-up","Digital checklists","Professional brand"],"benefit":"Close More Listings"},
 {"id":"05","name":"Insurance Agency","title":"Insurance Agency Business Kit","sub":"Policy & Client Management System","pri":"#1B2A4A","acc":"#2980B9","files":44,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Policy Tracker","Client Portal","Renewal Calendar","Quote Templates","Claims Log","Sales Pipeline","Compliance Docs","Growth Planner"],"pillars":["Prospect Management","Quote Process","Policy Onboarding","Renewal System","Agency Growth"],"before":["No renewal alerts","Scattered policies","Manual quotes","Client data chaos"],"after":["Automated renewals","Unified dashboard","Quote calculator","Clean database"],"benefit":"Retain More Clients"},
 {"id":"06","name":"AI Social Media","title":"AI Social Media Marketing Kit","sub":"Content Creation & Growth System","pri":"#1A0533","acc":"#FF006E","files":55,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Content Calendar","AI Prompt Library","Caption Templates","Hashtag Vault","Analytics Tracker","Story Templates","Reel Scripts","Brand Guidelines"],"pillars":["Content Strategy","AI Copywriting","Visual Branding","Posting Schedule","Analytics & Growth"],"before":["Blank content calendar","No posting strategy","Generic captions","Zero engagement"],"after":["30-day content plan","AI-powered scripts","Brand-consistent posts","Viral frameworks"],"benefit":"Grow Faster with AI"},
 {"id":"07","name":"Bookkeeper Launch","title":"Bookkeeper Business Launch Kit","sub":"Start & Scale Your Practice","pri":"#006D6D","acc":"#FF6B6B","files":43,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Business Setup Guide","Pricing Calculator","Client Contracts","Service Packages","Tech Stack Guide","Marketing Plan","Client Onboarding","Proposal Templates"],"pillars":["Business Foundation","Service Pricing","Client Acquisition","Onboarding System","Revenue Scaling"],"before":["No business structure","Undercharging clients","No marketing plan","Informal agreements"],"after":["LLC ready framework","Premium pricing","Lead gen system","Professional contracts"],"benefit":"Launch in 30 Days"},
 {"id":"08","name":"Staffing Agency","title":"Staffing Agency Starter Kit","sub":"Recruiting & Placement System","pri":"#0D1B2A","acc":"#C9A84C","files":48,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Candidate Tracker","Client Contracts","Job Order Forms","Timesheet Templates","Invoice System","Background Check Log","Compliance Docs","Revenue Dashboard"],"pillars":["Client Development","Job Orders","Candidate Pipeline","Placement Process","Financial Management"],"before":["No candidate system","Manual timesheets","Missed placements","No contracts"],"after":["Digital ATS","Auto-calculated pay","Placement tracker","Legal templates"],"benefit":"Build a Staffing Empire"},
 {"id":"09","name":"AI Automation","title":"AI Automation Agency Kit","sub":"Client Automation & Delivery System","pri":"#0B0C2A","acc":"#7C3AED","files":56,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Service Catalog","Automation Blueprints","Client Proposals","SOW Templates","Delivery Tracker","Pricing Calculator","Tech Stack Guide","Case Studies"],"pillars":["Service Design","Sales Process","Project Delivery","Client Results","Agency Scaling"],"before":["No productized offer","Unclear pricing","Long sales cycles","No delivery system"],"after":["Clear AI packages","Fixed fee pricing","Streamlined delivery","Repeatable results"],"benefit":"Sell AI Services Fast"},
 {"id":"10","name":"Virtual Assistant","title":"Virtual Assistant Business Kit","sub":"Client & Service Management System","pri":"#2D3748","acc":"#38A169","files":46,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Service Menu","Client Portal","Time Tracker","Task Templates","Invoice Builder","Niche Finder","Rate Calculator","Marketing Kit"],"pillars":["Niche Selection","Service Packages","Client Onboarding","Time Management","Business Growth"],"before":["No niche defined","Hourly undercharging","No client system","Random tasks"],"after":["Profitable niche","Package pricing","Clear contracts","Organized workflow"],"benefit":"Get Booked Out Fast"},
 {"id":"11","name":"Airbnb CoHost","title":"Airbnb Co-Host Business Kit","sub":"Property & Guest Management System","pri":"#C0392B","acc":"#00A699","files":44,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Property Checklist","Guest Welcome Guide","Pricing Calculator","Maintenance Log","Co-Host Agreement","Review Templates","Turnover Checklist","Income Tracker"],"pillars":["Property Onboarding","Guest Experience","Pricing Strategy","Operations","Revenue Growth"],"before":["Manual guest messages","No pricing system","Missed maintenance","Inconsistent service"],"after":["Auto-message templates","Dynamic pricing","Maintenance schedule","5-star process"],"benefit":"Maximize Your Properties"},
 {"id":"12","name":"Notion Portal","title":"Notion Business Portal Bundle","sub":"Complete Workspace & Client System","pri":"#191919","acc":"#6366F1","files":42,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["CRM Database","Project Tracker","Client Portal","Invoice Templates","Content Calendar","SOPs Library","Team Wiki","Goal Tracker"],"pillars":["Workspace Setup","Client Management","Project Delivery","Team Collaboration","Business Systems"],"before":["Tools scattered everywhere","No client visibility","Missed deadlines","Disorganized SOPs"],"after":["All-in-one workspace","Client self-service","Automated tracking","Documented systems"],"benefit":"Work Smarter in Notion"},
 {"id":"13","name":"UGC Creator","title":"UGC Creator Brand Deal Kit","sub":"Pitch, Negotiate & Deliver Content","pri":"#1A1A2E","acc":"#E94560","files":50,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Media Kit Template","Rate Card Builder","Brand Pitch Deck","Contract Templates","Content Brief","Deliverable Tracker","Invoice System","Niche Audit"],"pillars":["Brand Identity","Pitching Brands","Deal Negotiation","Content Delivery","Scaling Income"],"before":["No media kit","Accepting low rates","Verbal agreements","No deliverable tracking"],"after":["Professional portfolio","Confident rate cards","Legal contracts","Organized delivery"],"benefit":"Land $1K+ Brand Deals"},
 {"id":"14","name":"Sponsorship Tracker","title":"Content Creator Sponsorship Kit","sub":"Income & Brand Deal Management","pri":"#0F2940","acc":"#FF6B35","files":53,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Deal Pipeline","Income Dashboard","Tax Tracker","Brand Contact CRM","Platform Analytics","Content Calendar","Rate Calculator","Pitch Templates"],"pillars":["Brand Pipeline","Deal Tracking","Income Management","Content Planning","Creator Growth"],"before":["Lost brand contacts","Untracked income","No tax preparation","Scattered content"],"after":["Full deal dashboard","Auto income log","Tax-ready reports","Content system"],"benefit":"Maximize Creator Income"},
 {"id":"15","name":"Etsy SEO","title":"Etsy Seller AI SEO System","sub":"Rank, Convert & Scale on Etsy","pri":"#F56400","acc":"#1A1A2E","files":58,"formats":["XLSX","DOCX","PDF","PPTX","CSV"],"feats":["Keyword Research Kit","Title Templates","Tag Vault","AI Prompt Library","Listing Optimizer","Photo Checklist","Pricing Calculator","Shop Audit"],"pillars":["Keyword Research","Listing Optimization","Visual Strategy","Pricing & Profit","Shop Scaling"],"before":["Zero search visibility","Generic titles","Wrong tags","Low conversion"],"after":["Page 1 rankings","AI-optimized titles","Trending tags","High conversion"],"benefit":"Rank #1 on Etsy"},
]

# ── Slide 1: Hero ─────────────────────────────────────────────
def slide_hero(p):
    img=Image.new('RGB',(SIZE,SIZE),h2r(p['pri']))
    draw=ImageDraw.Draw(img)
    grad_v(draw,0,0,SIZE,SIZE,p['pri'],r2h(lighten(p['pri'],0.22)))
    # diagonal accent block
    acc_l=lighten(p['acc'],0.15)
    draw.polygon([(int(SIZE*0.58),0),(SIZE,0),(SIZE,int(SIZE*0.48)),(int(SIZE*0.68),int(SIZE*0.52))],fill=acc_l)
    # dot texture on accent
    dots(draw,int(SIZE*0.58),0,SIZE,int(SIZE*0.55),darken(p['acc'],0.2),sp=60,r=5)
    # top accent stripe
    draw.rectangle([0,0,SIZE,18],fill=h2r(p['acc']))
    # BADGE top-left
    fb38=F('bold',38); fb30=F('bold',30)
    rr(draw,[60,42,390,88],10,fill=h2r(p['acc']))
    tcx(draw,"DIGITAL BUSINESS KIT",225,65,fb30,h2r(p['pri']))
    # Giant title
    words=p['title'].upper().split()
    if len(words)<=2: lines=words
    elif len(words)==3: lines=words
    elif len(words)==4: lines=[words[0]+' '+words[1],words[2],words[3]]
    else: lines=[' '.join(words[:2]),' '.join(words[2:4]),' '.join(words[4:])]
    lines=[l for l in lines if l]
    for fs in [144,120,100,84]:
        ff=F('serif',fs)
        if all(draw.textbbox((0,0),l,font=ff)[2]<SIZE-100 for l in lines):
            chosen=ff; break
    else: chosen=F('serif',84)
    ty=170; lg=int(chosen.size*1.08)
    for i,l in enumerate(lines):
        bb=draw.textbbox((0,0),l,font=chosen)
        draw.text((63,ty+i*lg+3),l,font=chosen,fill=darken(p['pri'],0.4))
        draw.text((60,ty+i*lg),l,font=chosen,fill=(255,255,255))
    sub_y=ty+len(lines)*lg+28
    fsub=F('reg',52)
    draw.text((62,sub_y),p['sub'],font=fsub,fill=h2r(p['acc']))
    draw.rectangle([62,sub_y+68,420,sub_y+72],fill=h2r(p['acc']))
    # Feature cards 2×4
    feats=p['feats'][:8]; fc_y=sub_y+110
    cw2=(SIZE-140)//4; ch2=90; cgap=20
    fb26=F('bold',26); fb34=F('bold',34)
    for i,feat in enumerate(feats):
        col=i%4; row=i//4
        cx2=60+col*(cw2+cgap); cy2=fc_y+row*(ch2+18)
        img=shadow(img,[cx2,cy2,cx2+cw2,cy2+ch2],r=10,off=6,blur=12,a=55)
        draw=ImageDraw.Draw(img)
        rr(draw,[cx2,cy2,cx2+cw2,cy2+ch2],10,fill=(255,255,255))
        rr(draw,[cx2,cy2,cx2+8,cy2+ch2],10,fill=h2r(p['acc']))
        draw.rectangle([cx2+4,cy2,cx2+8,cy2+ch2],fill=h2r(p['acc']))
        draw.text((cx2+18,cy2+8),f"{i+1:02d}",font=fb34,fill=h2r(p['acc']))
        wf=feat.split()
        if len(wf)<=2: draw.text((cx2+72,cy2+20),feat,font=fb26,fill=h2r(p['pri']))
        else:
            draw.text((cx2+72,cy2+8),' '.join(wf[:2]),font=fb26,fill=h2r(p['pri']))
            draw.text((cx2+72,cy2+42),' '.join(wf[2:]),font=fb26,fill=h2r(p['pri']))
    # Files badge
    badge_y=fc_y+2*ch2+2*18+30
    fs_num=F('serif',160); fs_lbl=F('bold',54)
    cnt=f"{p['files']}+"
    bb=draw.textbbox((0,0),cnt,font=fs_num)
    cntw=bb[2]-bb[0]
    bx=SIZE-cntw-80
    draw.text((bx+3,badge_y+3),cnt,font=fs_num,fill=darken(p['pri'],0.5))
    draw.text((bx,badge_y),cnt,font=fs_num,fill=(255,255,255))
    lbl_bb=draw.textbbox((0,0),"EDITABLE FILES",font=fs_lbl)
    lbl_x=bx+(cntw-(lbl_bb[2]-lbl_bb[0]))//2
    draw.text((lbl_x,badge_y+int(fs_num.size*0.88)),"EDITABLE FILES",font=fs_lbl,fill=h2r(p['acc']))
    # bottom bar
    draw.rectangle([0,SIZE-64,SIZE,SIZE],fill=h2r(p['acc']))
    fb36=F('bold',36)
    draw.text((60,SIZE-48),' • '.join(p['formats']),font=fb36,fill=h2r(p['pri']))
    return img

# ── Slide 2: What's Inside ────────────────────────────────────
def slide_inside(p):
    img=Image.new('RGB',(SIZE,SIZE),(248,249,252))
    draw=ImageDraw.Draw(img)
    pw=int(SIZE*0.38)
    grad_v(draw,0,0,pw,SIZE,p['pri'],r2h(lighten(p['pri'],0.28)))
    dots(draw,0,0,pw,SIZE,lighten(p['pri'],0.5),sp=58,r=4)
    draw.rectangle([0,0,SIZE,14],fill=h2r(p['acc']))
    fb36=F('bold',36); fb90=F('serif',90); fb70=F('serif',70)
    fb90b=F('bold',90); fb34=F('reg',34); fb30=F('bold',30)
    draw.text((55,44),"WHAT'S INSIDE",font=fb36,fill=h2r(p['acc']))
    nm=p['name'].upper().split()
    nf=fb70 if len(p['name'])>14 else fb90
    y0=120
    for i,w2 in enumerate(nm):
        draw.text((55,y0+i*int(nf.size*1.05)),w2,font=nf,fill=(255,255,255))
    draw.line([55,y0+len(nm)*int(nf.size*1.05)+10,pw-55,y0+len(nm)*int(nf.size*1.05)+14],fill=h2r(p['acc']),width=4)
    sy=y0+len(nm)*int(nf.size*1.05)+40
    draw.text((55,sy),f"{p['files']}+",font=fb90b,fill=h2r(p['acc']))
    draw.text((55,sy+int(fb90b.size*0.88)),"EDITABLE FILES",font=fb34,fill=(190,215,215))
    sy2=sy+int(fb90b.size*0.88)+50
    draw.text((55,sy2),str(len(p['formats'])),font=fb90b,fill=(255,255,255))
    draw.text((55,sy2+int(fb90b.size*0.88)),"FILE FORMATS",font=fb34,fill=(190,215,215))
    by=sy2+int(fb90b.size*0.88)+70
    for fmt in p['formats']:
        fw2=draw.textbbox((0,0),fmt,font=fb30)[2]+26
        rr(draw,[55,by,55+fw2,by+48],10,fill=h2r(p['acc']))
        draw.text((67,by+10),fmt,font=fb30,fill=h2r(p['pri']))
        by+=65
    draw.text((55,SIZE-90),"✓ Instant Download",font=fb34,fill=(190,240,190))
    draw.text((55,SIZE-46),"✓ Fully Editable",font=fb34,fill=(190,240,190))
    # right: 2×4 feature cards
    rs=pw+44; rw=SIZE-rs-44
    cw2=(rw-24)//2; ch2=(SIZE-80-24*3)//4; cgap=24
    fb32=F('bold',32); fb48=F('bold',48); fb26=F('reg',26)
    descs=["Organize & track","Professional templates","Client management","Revenue tracking","Marketing system","Automated workflow","Growth planning","Business operations"]
    for i,feat in enumerate(p['feats'][:8]):
        col=i%2; row=i//2
        cx2=rs+col*(cw2+cgap); cy2=40+row*(ch2+cgap)
        img=shadow(img,[cx2,cy2,cx2+cw2,cy2+ch2],r=14,off=8,blur=14,a=45)
        draw=ImageDraw.Draw(img)
        rr(draw,[cx2,cy2,cx2+cw2,cy2+ch2],14,fill=(255,255,255))
        rr(draw,[cx2,cy2,cx2+cw2,cy2+7],14,fill=h2r(p['acc']))
        draw.rectangle([cx2,cy2+4,cx2+cw2,cy2+7],fill=h2r(p['acc']))
        rr(draw,[cx2+20,cy2+18,cx2+74,cy2+72],12,fill=h2r(p['pri']))
        tcx(draw,f"{i+1:02d}",cx2+47,cy2+45,fb48,h2r(p['acc']))
        draw.text((cx2+88,cy2+18),feat,font=fb32,fill=h2r(p['pri']))
        draw.text((cx2+88,cy2+60),descs[i],font=fb26,fill=(110,110,130))
        draw.text((cx2+cw2-54,cy2+18),"✓",font=fb32,fill=h2r(p['acc']))
    return img

# ── Slide 3: Content Preview ──────────────────────────────────
def slide_preview(p):
    img=Image.new('RGB',(SIZE,SIZE),(242,244,248))
    draw=ImageDraw.Draw(img)
    grad_v(draw,0,0,SIZE,170,p['pri'],r2h(lighten(p['pri'],0.18)))
    draw.rectangle([0,0,SIZE,12],fill=h2r(p['acc']))
    fb38=F('bold',38); freg44=F('reg',44)
    draw.text((60,34),"CONTENT PREVIEW",font=fb38,fill=h2r(p['acc']))
    draw.text((60,88),"See exactly what you get inside",font=freg44,fill=(200,220,255))
    pad=55; gap=38; cols=3; rows=2
    tw=(SIZE-2*pad-gap*(cols-1))//cols
    th=(SIZE-200-2*pad-gap*(rows-1))//rows
    mocks=[mock_excel,mock_word,mock_pdf,mock_pptx,mock_csv,
           lambda im,x,y,w,h,pri,acc: mock_excel(im,x,y,w,h,acc,pri)]
    mlbls=["Spreadsheet Tracker","Strategy Document","PDF Guide","Presentation Deck","CSV Data Export","Dashboard Workbook"]
    fb32=F('bold',32)
    for i in range(6):
        col=i%cols; row=i//cols
        mx=pad+col*(tw+gap); my=200+row*(th+gap)
        img=shadow(img,[mx,my,mx+tw,my+th],r=12,off=8,blur=14,a=50)
        draw=ImageDraw.Draw(img)
        img=mocks[i](img,mx,my,tw,th,p['pri'],p['acc'])
        draw=ImageDraw.Draw(img)
        lbl=mlbls[i]
        lb=draw.textbbox((0,0),lbl,font=fb32)
        lw2=lb[2]-lb[0]
        draw.text((mx+tw//2-lw2//2,my+th+10),lbl,font=fb32,fill=(55,60,80))
    return img

# ── Slide 4: The System ───────────────────────────────────────
def slide_system(p):
    img=Image.new('RGB',(SIZE,SIZE),h2r(p['pri']))
    draw=ImageDraw.Draw(img)
    grad_v(draw,0,0,SIZE,SIZE,p['pri'],r2h(darken(p['pri'],0.35)))
    dots(draw,0,0,SIZE,SIZE,lighten(p['pri'],0.22),sp=65,r=5)
    draw.rectangle([0,0,SIZE,14],fill=h2r(p['acc']))
    fb38=F('bold',38); fs88=F('serif',88); fs72=F('serif',72)
    fb72=F('bold',72); fb44=F('bold',44); freg32=F('reg',32)
    draw.text((60,44),"THE SYSTEM",font=fb38,fill=h2r(p['acc']))
    nf=fs72 if len(p['name'])>14 else fs88
    draw.text((60,100),p['name'].upper(),font=nf,fill=(255,255,255))
    dy=100+int(nf.size*1.02)+20
    draw.rectangle([60,dy,460,dy+4],fill=h2r(p['acc']))
    bsy=dy+52; bh=168; bgap=32; bw=SIZE-130
    for i,pil in enumerate(p['pillars'][:5]):
        by=bsy+i*(bh+bgap)
        img=shadow(img,[60,by,60+bw,by+bh],r=14,off=8,blur=16,a=55)
        draw=ImageDraw.Draw(img)
        bar_c=lighten(p['pri'],0.14)
        rr(draw,[60,by,60+bw,by+bh],14,fill=bar_c)
        nw=130
        rr(draw,[60,by,60+nw,by+bh],14,fill=h2r(p['acc']))
        draw.rectangle([60+nw-14,by,60+nw,by+bh],fill=h2r(p['acc']))
        nb=draw.textbbox((0,0),str(i+1),font=fb72)
        tcx(draw,str(i+1),60+nw//2,by+bh//2,fb72,h2r(p['pri']))
        draw.text((60+nw+28,by+22),pil.upper(),font=fb44,fill=(255,255,255))
        draw.line([60+nw+28,by+bh//2,60+bw-28,by+bh//2],fill=lighten(p['pri'],0.35),width=1)
        fi=p['feats'][i%len(p['feats'])]
        draw.text((60+nw+28,by+bh//2+18),f"→ {fi}",font=freg32,fill=lighten(p['acc'],0.45))
        pg_x=60+bw-210; pg_v=(5-i)/5
        rr(draw,[pg_x,by+bh//2-14,pg_x+170,by+bh//2+14],7,fill=lighten(p['pri'],0.28))
        rr(draw,[pg_x,by+bh//2-14,pg_x+int(170*pg_v),by+bh//2+14],7,fill=h2r(p['acc']))
    fb36=F('bold',36); freg30=F('reg',30)
    draw.text((60,SIZE-84),"STEP-BY-STEP BUSINESS SYSTEM",font=fb36,fill=h2r(p['acc']))
    draw.text((60,SIZE-40),f"Complete {p['name']} Framework",font=freg30,fill=lighten(p['pri'],0.6))
    return img

# ── Slide 5: Benefits ─────────────────────────────────────────
def slide_benefits(p):
    img=Image.new('RGB',(SIZE,SIZE),(248,249,252))
    draw=ImageDraw.Draw(img)
    draw.rectangle([0,0,SIZE,14],fill=h2r(p['acc']))
    fb38=F('bold',38); fs96=F('serif',96); fs78=F('serif',78)
    fb40=F('bold',40); freg36=F('reg',36); fs140=F('serif',140)
    fb42=F('bold',42); fb38b=F('bold',38); freg30=F('reg',30)
    draw.text((60,44),"WHAT YOU GET",font=fb38,fill=h2r(p['acc']))
    nf=fs78 if len(p['name'])>12 else fs96
    draw.text((60,104),p['name'].upper(),font=nf,fill=h2r(p['pri']))
    draw.rectangle([60,104+int(nf.size*1.02)+8,480,104+int(nf.size*1.02)+12],fill=h2r(p['acc']))
    items=p['after'][:6]
    ciy=104+int(nf.size*1.02)+48; cih=115; ciw=int(SIZE*0.56)
    for i,item in enumerate(items):
        cy2=ciy+i*cih
        draw.ellipse([60,cy2+14,132,cy2+86],fill=h2r(p['pri']))
        tcx(draw,"✓",96,cy2+50,fb40,h2r(p['acc']))
        draw.text((148,cy2+26),item,font=freg36,fill=(38,40,60))
        if i<len(items)-1:
            draw.line([60,cy2+cih-6,ciw,cy2+cih-6],fill=(215,218,228),width=1)
    # price card
    cx2=int(SIZE*0.61); cy2=120; cw2=SIZE-cx2-60; ch2=SIZE-180
    img=shadow(img,[cx2,cy2,cx2+cw2,cy2+ch2],r=22,off=12,blur=20,a=55)
    draw=ImageDraw.Draw(img)
    rr(draw,[cx2,cy2,cx2+cw2,cy2+ch2],22,fill=h2r(p['pri']))
    grad_v(draw,cx2+4,cy2+4,cx2+cw2-4,cy2+ch2-4,p['pri'],r2h(lighten(p['pri'],0.32)))
    rr(draw,[cx2,cy2,cx2+cw2,cy2+ch2],22,outline=h2r(p['acc']),width=5)
    dots(draw,cx2,cy2,cx2+cw2,cy2+ch2,lighten(p['pri'],0.28),sp=50,r=3)
    tcx(draw,"TOTAL VALUE",cx2+cw2//2,cy2+88,fb42,h2r(p['acc']))
    tcx(draw,"$247",cx2+cw2//2,cy2+230,fs140,(255,255,255))
    draw.line([cx2+44,cy2+338,cx2+cw2-44,cy2+338],fill=h2r(p['acc']),width=2)
    ff=p['feats'][:5]; ffreg=F('reg',30)
    for i,f2 in enumerate(ff):
        fy=cy2+370+i*72
        if fy>cy2+ch2-110: break
        rr(draw,[cx2+34,fy,cx2+62,fy+28],5,fill=h2r(p['acc']))
        draw.text((cx2+76,fy+2),f2,font=ffreg,fill=lighten(p['pri'],0.8))
    bty=cy2+ch2-102
    rr(draw,[cx2+32,bty,cx2+cw2-32,bty+72],16,fill=h2r(p['acc']))
    tcx(draw,"INSTANT DOWNLOAD",cx2+cw2//2,bty+36,fb38b,h2r(p['pri']))
    return img

# ── Slide 6: Before / After ───────────────────────────────────
def slide_before_after(p):
    img=Image.new('RGB',(SIZE,SIZE),h2r(p['pri']))
    draw=ImageDraw.Draw(img)
    # Split using polygon: left=dark red, right=primary gradient
    sxt=int(SIZE*0.42); sxb=int(SIZE*0.58)
    draw.polygon([(0,0),(sxt,0),(sxb,SIZE),(0,SIZE)],fill=(95,15,15))
    draw.polygon([(sxt,0),(SIZE,0),(SIZE,SIZE),(sxb,SIZE)],fill=h2r(p['pri']))
    # Gradient on right half
    for y2 in range(SIZE):
        t=y2/SIZE; c=mix(p['pri'],r2h(lighten(p['pri'],0.22)),t)
        sx=int(sxt+(sxb-sxt)*(y2/SIZE))
        draw.line([(sx,y2),(SIZE,y2)],fill=c)
    # diagonal divider
    draw.line([(sxt,0),(sxb,SIZE)],fill=(255,255,255),width=10)
    fs88=F('serif',88); fb48=F('bold',48); freg38=F('reg',38)
    tcx(draw,"BEFORE",SIZE//4,130,fs88,(255,255,255))
    draw.line([60,200,sxt-40,204],fill=(200,80,80),width=4)
    for i,item in enumerate(p['before'][:4]):
        iy=260+i*160; cx2=SIZE//4
        draw.ellipse([cx2-42,iy-42,cx2+42,iy+42],outline=(255,90,90),width=4)
        tcx(draw,"✗",cx2,iy,fb48,(255,90,90))
        lines=[item] if len(item)<=22 else [item[:22],item[22:]]
        for j,l in enumerate(lines):
            lb=draw.textbbox((0,0),l,font=freg38); lw2=lb[2]-lb[0]
            draw.text((cx2-lw2//2,iy+56+j*44),l,font=freg38,fill=(255,200,200))
    tcx(draw,"AFTER",SIZE*3//4,130,fs88,(255,255,255))
    draw.line([sxb+40,200,SIZE-60,204],fill=h2r(p['acc']),width=4)
    fb48c=F('bold',48)
    for i,item in enumerate(p['after'][:4]):
        iy=260+i*160; cx2=SIZE*3//4
        draw.ellipse([cx2-42,iy-42,cx2+42,iy+42],fill=h2r(p['acc']))
        tcx(draw,"✓",cx2,iy,fb48c,(255,255,255))
        lines=[item] if len(item)<=22 else [item[:22],item[22:]]
        for j,l in enumerate(lines):
            lb=draw.textbbox((0,0),l,font=freg38); lw2=lb[2]-lb[0]
            draw.text((cx2-lw2//2,iy+56+j*44),l,font=freg38,fill=(255,255,255))
    # bottom banner
    draw.rectangle([0,SIZE-104,SIZE,SIZE],fill=h2r(p['acc']))
    fb52=F('bold',52)
    tcx(draw,p['benefit'].upper()+" — WITH THIS SYSTEM",SIZE//2,SIZE-52,fb52,h2r(p['pri']))
    return img

# ── Slide 7: Easy to Use ──────────────────────────────────────
def slide_easy(p):
    img=Image.new('RGB',(SIZE,SIZE),(244,245,250))
    draw=ImageDraw.Draw(img)
    draw.rectangle([0,0,SIZE,14],fill=h2r(p['acc']))
    grad_v(draw,0,0,SIZE,210,p['pri'],r2h(lighten(p['pri'],0.12)))
    fb38=F('bold',38); fs78=F('serif',78)
    draw.text((60,36),"EASY TO USE",font=fb38,fill=h2r(p['acc']))
    draw.text((60,92),"WORKS ON ALL DEVICES",font=fs78,fill=(255,255,255))
    # Laptop (center-left)
    img=laptop(img,int(SIZE*0.36),int(SIZE*0.54),740,p['pri'],p['acc'],
               p['name'],p['sub'][:28],p['files'])
    draw=ImageDraw.Draw(img)
    # Phone (right of laptop)
    img=phone(img,int(SIZE*0.74),int(SIZE*0.50),230,p['pri'],p['acc'])
    draw=ImageDraw.Draw(img)
    # Feature list (bottom-right area)
    easys=[("No Experience Needed","Plug & play templates"),("Works in Any App","Excel, Google Sheets & Word"),("Instant Download","Ready to use in 60 seconds"),("Full Instructions","Step-by-step guide included")]
    fx=int(SIZE*0.5); fy=int(SIZE*0.78)
    fb34=F('bold',34); freg28=F('reg',28)
    for i,(t2,d2) in enumerate(easys):
        cy2=fy+i*96
        if cy2>SIZE-70: break
        draw.ellipse([fx-46,cy2-4,fx-6,cy2+36],fill=h2r(p['acc']))
        tcx(draw,"✓",fx-26,cy2+16,F('bold',26),(255,255,255))
        draw.text((fx+4,cy2),t2,font=fb34,fill=h2r(p['pri']))
        draw.text((fx+4,cy2+40),d2,font=freg28,fill=(100,105,125))
    # Format badges
    bx=60; by=SIZE-102; fb30=F('bold',30)
    for fmt in p['formats']:
        fw2=draw.textbbox((0,0),fmt,font=fb30)[2]+28
        rr(draw,[bx,by,bx+fw2,by+52],11,fill=h2r(p['pri']))
        draw.text((bx+14,by+12),fmt,font=fb30,fill=h2r(p['acc']))
        bx+=fw2+18
    return img

# ── Generate all images ───────────────────────────────────────
slides=[(slide_hero,"01_Hero_Cover"),(slide_inside,"02_Whats_Inside"),
        (slide_preview,"03_Content_Preview"),(slide_system,"04_The_System"),
        (slide_benefits,"05_Benefits"),(slide_before_after,"06_Before_After"),
        (slide_easy,"07_Easy_To_Use")]

total=len(PRODUCTS)*len(slides); done=0

for p in PRODUCTS:
    folder=os.path.join(OUT,f"{p['id']}_{p['name'].replace(' ','_')}")
    os.makedirs(folder,exist_ok=True)
    for fn,sname in slides:
        try:
            img=fn(p)
            img.save(os.path.join(folder,f"{sname}.png"),'PNG')
            done+=1
            print(f"[{done}/{total}] {p['id']} {sname}")
        except Exception as e:
            print(f"  ERROR {p['id']} {sname}: {e}")
            traceback.print_exc()
    # ZIP
    zp=os.path.join(OUT,f"{p['id']}_{p['name'].replace(' ','_')}_images.zip")
    with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(os.listdir(folder)):
            if f.endswith('.png'):
                zf.write(os.path.join(folder,f),f)
    print(f"  ZIP -> {zp}")

print(f"\nComplete: {done}/{total} images generated.")
