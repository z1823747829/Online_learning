import{d as G,u as K,Q as L,A as Q,r as Y,$ as Z,a0 as j,a1 as H,o as c,n as h,w as r,b,K as J,a as s,c as _,g as o,h as n,t as i,D as d,f as y,F as v,i as O,Y as V,a2 as W,a3 as $,z as X,v as ee,m as te,y as oe,I as se,E as ae,e as re,a4 as le,a5 as ne,G as ce,a6 as ie,a7 as ue,Z as de,a8 as _e,q as me,s as pe,_ as fe}from"./index-61080a5f.js";/* empty css               *//* empty css                   *//* empty css                 *//* empty css                 *//* empty css                   *//* empty css                     *//* empty css                *//* empty css               *//* empty css                   *//* empty css               */import{g as ge}from"./my_function-9ea274aa.js";const w=p=>(me("data-v-c1957cf2"),p=p(),pe(),p),he=["src"],be=["src"],ye={style:{"font-size":"5px"}},ve={class:"profile"},we={style:{width:"100%","text-align":"left"}},Ee={style:{display:"inline-block"}},ke=w(()=>n("br",null,null,-1)),xe={style:{"font-size":"12px",color:"gray"}},Te=w(()=>n("br",null,null,-1)),Ce=w(()=>n("br",null,null,-1)),Ve={class:"dialog-footer"},$e=G({__name:"CourseResource",setup(p){const B=K(),E=L(),u=Q();let e=Y({tab:"first",dialog:!1,course:O,time:0,course_resource:V,course_resources:[V],comments:[W],form:{c_id:0,content:""}});const I=Z(()=>{let t=e.course_resource.resource_file.split(".");return t[t.length-1]==="pdf"}),g=()=>{b.get(`/api/web/course/resource/${E.params.crid}`).then(t=>{t.data.status===!0?(e.course=t.data.course,e.course_resource=t.data.course_resource,e.course_resources=t.data.course_resources,e.comments=t.data.comments,e.form.c_id=e.course.id,e.time=t.data.time):console.log("error")}).catch(t=>{console.log(t)})},R=()=>{if(e.form.content===""){$({message:"请输入评论",type:"warning"});return}b.post("/api/web/comment/add",e.form,{headers:{"Content-Type":"multipart/form-data"}}).then(t=>{t.data.status===!0?($({message:"评论成功",type:"success"}),e.form.content="",g()):console.log("error")}).catch(t=>{console.log(t)})},S=()=>{var t,l,m;((t=u.value)==null?void 0:t.currentTime)==0&&(u.value.currentTime=e.time),(((l=u.value)==null?void 0:l.currentTime)-e.time>10||e.time-((m=u.value)==null?void 0:m.currentTime)>10)&&(e.time=u.value.currentTime,b.post(`/api/web/course/resource/${E.params.crid}/set_time`,{time:e.time},{headers:{"Content-Type":"multipart/form-data"}}))};return j((t,l)=>{t.params.crid!==l.params.crid&&setTimeout(g,100)}),H(()=>{u.value.currentTime=e.time}),e.comments=[],e.course_resources=[],g(),(t,l)=>{const m=X,U=ee,k=te,D=de,z=oe,f=se,x=ae,T=re,C=le,A=_e,N=ne,F=ce,M=ie,P=ue,q=J;return c(),h(q,{style:{height:"100%"}},{default:r(()=>[s(m,{span:18,style:{height:"100%",overflow:"hidden"}},{default:r(()=>[I.value?(c(),_("iframe",{key:0,src:o(e).course_resource.resource_file,height:"100%",width:"100%"},null,8,he)):(c(),_("video",{key:1,ref_key:"video",ref:u,style:{height:"100%",width:"100%"},src:o(e).course_resource.resource_file,onTimeupdate:S,autoplay:"",controls:""}," 您的浏览器不支持 video 标签。 ",40,be))]),_:1}),s(m,{span:6,style:{padding:"0 10px",height:"100%"}},{default:r(()=>[s(P,{modelValue:o(e).tab,"onUpdate:modelValue":l[5]||(l[5]=a=>o(e).tab=a),class:"tab"},{default:r(()=>[s(C,{label:"详情",name:"first"},{default:r(()=>[s(x,{class:"el-scrollbar first"},{default:r(()=>[s(z,null,{default:r(()=>[s(U,{src:o(e).course.img,style:{width:"100%"}},null,8,["src"]),n("h2",null,i(o(e).course.course),1),n("span",ye,"教师："+i(o(e).course.teacher)+" 点击量："+i(o(e).course.clicks),1),s(k,{"content-position":"left"},{default:r(()=>[d("课程详情")]),_:1}),n("p",ve,i(o(e).course.profile),1),(c(!0),_(v,null,y(o(e).course.keyword,a=>(c(),h(D,{class:"tag"},{default:r(()=>[d(i(a),1)]),_:2},1024))),256))]),_:1}),s(k,{"content-position":"left"},{default:r(()=>[d("课程资源")]),_:1}),(c(!0),_(v,null,y(o(e).course_resources,a=>(c(),h(f,{type:"primary",plain:"",style:{width:"80%",margin:"5px",height:"50px"},onClick:Ie=>o(B).push(`/course/resource/${a.id}`)},{default:r(()=>[d(i(a.order+" : "+a.resource),1)]),_:2},1032,["onClick"]))),256))]),_:1}),s(T,{right:20,bottom:50,target:".first .el-scrollbar__wrap"})]),_:1}),s(C,{label:"评论",name:"second"},{default:r(()=>[s(x,{class:"el-scrollbar second"},{default:r(()=>[(c(!0),_(v,null,y(o(e).comments,a=>(c(),_("div",we,[s(A,{src:a.user.head},null,8,["src"]),n("div",Ee,[n("span",null,i(a.user.nickname),1),ke,n("span",xe,i(o(ge)(a.time)),1),Te]),Ce,n("span",null,i(a.content),1)]))),256))]),_:1}),s(N,{position:"bottom",offset:20},{default:r(()=>[s(f,{type:"primary",onClick:l[0]||(l[0]=a=>o(e).dialog=!0)},{default:r(()=>[d("评论")]),_:1})]),_:1}),s(M,{modelValue:o(e).dialog,"onUpdate:modelValue":l[4]||(l[4]=a=>o(e).dialog=a),title:"评论","align-center":"",draggable:"",width:"40%"},{footer:r(()=>[n("span",Ve,[s(f,{onClick:l[2]||(l[2]=a=>o(e).dialog=!1)},{default:r(()=>[d("取消")]),_:1}),s(f,{type:"primary",onClick:l[3]||(l[3]=a=>{o(e).dialog=!1,R()})},{default:r(()=>[d("上传")]),_:1})])]),default:r(()=>[s(F,{modelValue:o(e).form.content,"onUpdate:modelValue":l[1]||(l[1]=a=>o(e).form.content=a),placeholder:"请输入评论",clearable:"",type:"textarea",rows:"4",maxlength:"128","show-word-limit":""},null,8,["modelValue"])]),_:1},8,["modelValue"]),s(T,{right:20,bottom:50,target:".second .el-scrollbar__wrap "})]),_:1})]),_:1},8,["modelValue"])]),_:1})]),_:1})}}});const Ke=fe($e,[["__scopeId","data-v-c1957cf2"]]);export{Ke as default};