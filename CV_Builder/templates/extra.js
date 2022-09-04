const addLang = document.querySelector('.addLang');
const addEdu = document.querySelector('.addEdu');
const addWork = document.querySelector('.addWork');
const addSkill = document.querySelector('.addSkill');
const lang=document.querySelector('.lang');
const edu=document.querySelector('.edu');
const work=document.querySelector('.work');
const skills=document.querySelector('.skills');

const generateLanguage = () =>{
    const html = `
                    <li>
                        <div class="col1">
                            <div>
                                <div class="col3">
                                    <label for="language">Dil</label>
                                    <input type="text" name="language" placeholder="ör. Türkçe">
                                </div>
                                <div class="col2">
                                    <label for="level">Seviye</label>
                                    <select name="level" id="" class="day">
                                        <option value="0">Seç</option>
                                        <option value="01">Ana Dil</option>
                                        <option value="02">A1</option>
                                        <option value="03">A2</option>
                                        <option value="04">A3</option>
                                        <option value="05">B1</option>
                                        <option value="06">B2</option>
                                        <option value="07">B3</option>
                                        <option value="08">C1</option>
                                        <option value="09">C2</option>
                                        <option value="10">C3</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                            </div>
                        </div>
                        <div class="button">
                            <button class="deleteLang">
                                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="svg--deleteLang" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path>
                                </svg>
                            </button>
                        </div>
                    </li>
    `;
    lang.innerHTML += html;
}
const generateEducation = () =>{
    const html = `
    <li>
        <div>
            <div class="extra">
                <div class="inline">
                    <div class="inner">
                        <div class="col1">
                            <div>
                                <div class="col3">
                                    <label for="school">Okul Adı</label>
                                    <input type="text" name="school" placeholder="ör. Boğaziçi Üniversitesi">
                                </div>
                                <div class="col2">
                                    <label for="location">Okulun Konumu</label>
                                    <input type="text" name="location" placeholder="ör. Levent, İstanbul, Türkiye">
                                </div>
                            </div>
                        </div>
                        <div class="col1">
                            <div>
                                <div class="col3">
                                    <label for="degree">Derece</label>
                                    <input type="text" name="degree" placeholder="ör. Lisans">
                                </div>
                                <div class="col2">
                                    <label for="field">Çalışma Alanı</label>
                                    <input type="text" name="field" placeholder="ör. Bilgisayar Mühendisliği">
                                </div>
                            </div>
                        </div>
                        <div class="col1">
                            <div class="col2">
                                <div class="ay">
                                    <label class="txt">Başlangıç Tarihi</label>
                                    <select name="aylar" class="day">
                                        <option value="0">Ay</option>
                                        <option value="01">Ocak</option>
                                        <option value="02">Şubat</option>
                                        <option value="03">Mart</option>
                                        <option value="04">Nisan</option>
                                        <option value="05">Mayıs</option>
                                        <option value="06">Haziran</option>
                                        <option value="07">Temmuz</option>
                                        <option value="08">Ağustos</option>
                                        <option value="09">Eylül</option>
                                        <option value="10">Ekim</option>
                                        <option value="11">Kasım</option>
                                        <option value="12">Aralık</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                                <div class="yil">
                                    <label class="txt">&nbsp;</label>
                                    <select name="yillar" class="day">
                                        <option value="0">Yıl</option>
                                        <option value="01">2022</option>
                                        <option value="02">2021</option>
                                        <option value="03">2020</option>
                                        <option value="04">2019</option>
                                        <option value="05">2018</option>
                                        <option value="06">2017</option>
                                        <option value="07">2016</option>
                                        <option value="08">2015</option>
                                        <option value="09">2014</option>
                                        <option value="10">2013</option>
                                        <option value="11">2012</option>
                                        <option value="12">2011</option>
                                        <option value="13">2010</option>
                                        <option value="14">2009</option>
                                        <option value="15">2008</option>
                                        <option value="16">2007</option>
                                        <option value="17">2006</option>
                                        <option value="18">2005</option>
                                        <option value="19">2004</option>
                                        <option value="20">2003</option>
                                        <option value="21">2002</option>
                                        <option value="22">2001</option>
                                        <option value="23">2000</option>
                                        <option value="24">1999</option>
                                        <option value="25">1998</option>
                                        <option value="26">1997</option>
                                        <option value="27">1996</option>
                                        <option value="28">1995</option>
                                        <option value="29">1994</option>
                                        <option value="30">1993</option>
                                        <option value="31">1992</option>
                                        <option value="32">1991</option>
                                        <option value="33">1990</option>
                                        <option value="34">1989</option>
                                        <option value="35">1988</option>
                                        <option value="36">1987</option>
                                        <option value="37">1986</option>
                                        <option value="38">1985</option>
                                        <option value="39">1984</option>
                                        <option value="40">1983</option>
                                        <option value="41">1982</option>
                                        <option value="42">1981</option>
                                        <option value="43">1980</option>
                                        <option value="44">1979</option>
                                        <option value="45">1978</option>
                                        <option value="46">1977</option>
                                        <option value="47">1976</option>
                                        <option value="48">1975</option>
                                        <option value="49">1974</option>
                                        <option value="50">1973</option>
                                        <option value="51">1972</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                            </div>
                            <div class="col2">
                                <div class="ay">
                                    <label class="txt">Bitiş Tarihi</label>
                                    <select name="aylar" class="day">
                                        <option value="0">Ay</option>
                                        <option value="01">Halen</option>
                                        <option value="02">Ocak</option>
                                        <option value="03">Şubat</option>
                                        <option value="04">Mart</option>
                                        <option value="05">Nisan</option>
                                        <option value="06">Mayıs</option>
                                        <option value="07">Haziran</option>
                                        <option value="08">Temmuz</option>
                                        <option value="09">Ağustos</option>
                                        <option value="10">Eylül</option>
                                        <option value="11">Ekim</option>
                                        <option value="12">Kasım</option>
                                        <option value="13">Aralık</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                                <div class="yil">
                                    <label class="txt">&nbsp;</label>
                                    <select name="yillar" class="day">
                                        <option value="0">Yıl</option>
                                        <option value="01">Halen</option>
                                        <option value="02">2022</option>
                                        <option value="03">2021</option>
                                        <option value="04">2020</option>
                                        <option value="05">2019</option>
                                        <option value="06">2018</option>
                                        <option value="07">2017</option>
                                        <option value="08">2016</option>
                                        <option value="09">2015</option>
                                        <option value="10">2014</option>
                                        <option value="11">2013</option>
                                        <option value="12">2012</option>
                                        <option value="13">2011</option>
                                        <option value="14">2010</option>
                                        <option value="15">2009</option>
                                        <option value="16">2008</option>
                                        <option value="17">2007</option>
                                        <option value="18">2006</option>
                                        <option value="19">2005</option>
                                        <option value="20">2004</option>
                                        <option value="21">2003</option>
                                        <option value="22">2002</option>
                                        <option value="23">2001</option>
                                        <option value="24">2000</option>
                                        <option value="25">1999</option>
                                        <option value="26">1998</option>
                                        <option value="27">1997</option>
                                        <option value="28">1996</option>
                                        <option value="29">1995</option>
                                        <option value="30">1994</option>
                                        <option value="31">1993</option>
                                        <option value="32">1992</option>
                                        <option value="33">1991</option>
                                        <option value="34">1990</option>
                                        <option value="35">1989</option>
                                        <option value="36">1988</option>
                                        <option value="37">1987</option>
                                        <option value="38">1986</option>
                                        <option value="39">1985</option>
                                        <option value="40">1984</option>
                                        <option value="41">1983</option>
                                        <option value="42">1982</option>
                                        <option value="43">1981</option>
                                        <option value="44">1980</option>
                                        <option value="45">1979</option>
                                        <option value="46">1978</option>
                                        <option value="47">1977</option>
                                        <option value="48">1976</option>
                                        <option value="49">1975</option>
                                        <option value="50">1974</option>
                                        <option value="51">1973</option>
                                        <option value="52">1972</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="button">
            <button class="deleteEdu">
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="svg--deleteEdu" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path>
                </svg>
            </button>
        </div>
    </li>
    `;
    edu.innerHTML += html;
}

const generateWork = () =>{
    const html = `
    <li>
        <div>
            <div class="extra">
                <div class="inline">
                    <div class="inner">
                        <div class="col1">
                            <div>
                                <div class="col3">
                                    <label for="title">İş Başlığı</label>
                                    <input type="text" name="title" placeholder="ör. Project Manager">
                                </div>
                                <div class="col2">
                                    <label for="company">Şirket Adı</label>
                                    <input type="text" name="company" placeholder="ör. HepsiBurada">
                                </div>
                            </div>
                        </div>
                        <div class="col1">
                            <div>
                                <div class="col3">
                                    <label for="city">Şehir</label>
                                    <input type="text" name="city" placeholder="ör. İstanbul">
                                </div>
                                <div class="col2">
                                    <label for="country">Ülke</label>
                                    <input type="text" name="country" placeholder="ör. Türkiye">
                                </div>
                            </div>
                        </div>
                        <div class="col1">
                            <div class="col2">
                                <div class="ay">
                                    <label class="txt">Başlangıç Tarihi</label>
                                    <select name="aylar" class="day">
                                        <option value="0">Ay</option>
                                        <option value="01">Ocak</option>
                                        <option value="02">Şubat</option>
                                        <option value="03">Mart</option>
                                        <option value="04">Nisan</option>
                                        <option value="05">Mayıs</option>
                                        <option value="06">Haziran</option>
                                        <option value="07">Temmuz</option>
                                        <option value="08">Ağustos</option>
                                        <option value="09">Eylül</option>
                                        <option value="10">Ekim</option>
                                        <option value="11">Kasım</option>
                                        <option value="12">Aralık</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                                <div class="yil">
                                    <label class="txt">&nbsp;</label>
                                    <select name="yillar" class="day">
                                        <option value="0">Yıl</option>
                                        <option value="01">2022</option>
                                        <option value="02">2021</option>
                                        <option value="03">2020</option>
                                        <option value="04">2019</option>
                                        <option value="05">2018</option>
                                        <option value="06">2017</option>
                                        <option value="07">2016</option>
                                        <option value="08">2015</option>
                                        <option value="09">2014</option>
                                        <option value="10">2013</option>
                                        <option value="11">2012</option>
                                        <option value="12">2011</option>
                                        <option value="13">2010</option>
                                        <option value="14">2009</option>
                                        <option value="15">2008</option>
                                        <option value="16">2007</option>
                                        <option value="17">2006</option>
                                        <option value="18">2005</option>
                                        <option value="19">2004</option>
                                        <option value="20">2003</option>
                                        <option value="21">2002</option>
                                        <option value="22">2001</option>
                                        <option value="23">2000</option>
                                        <option value="24">1999</option>
                                        <option value="25">1998</option>
                                        <option value="26">1997</option>
                                        <option value="27">1996</option>
                                        <option value="28">1995</option>
                                        <option value="29">1994</option>
                                        <option value="30">1993</option>
                                        <option value="31">1992</option>
                                        <option value="32">1991</option>
                                        <option value="33">1990</option>
                                        <option value="34">1989</option>
                                        <option value="35">1988</option>
                                        <option value="36">1987</option>
                                        <option value="37">1986</option>
                                        <option value="38">1985</option>
                                        <option value="39">1984</option>
                                        <option value="40">1983</option>
                                        <option value="41">1982</option>
                                        <option value="42">1981</option>
                                        <option value="43">1980</option>
                                        <option value="44">1979</option>
                                        <option value="45">1978</option>
                                        <option value="46">1977</option>
                                        <option value="47">1976</option>
                                        <option value="48">1975</option>
                                        <option value="49">1974</option>
                                        <option value="50">1973</option>
                                        <option value="51">1972</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                            </div>
                            <div class="col2">
                                <div class="ay">
                                    <label class="txt">Bitiş Tarihi</label>
                                    <select name="aylar" class="day">
                                        <option value="0">Ay</option>
                                        <option value="01">Halen</option>
                                        <option value="02">Ocak</option>
                                        <option value="03">Şubat</option>
                                        <option value="04">Mart</option>
                                        <option value="05">Nisan</option>
                                        <option value="06">Mayıs</option>
                                        <option value="07">Haziran</option>
                                        <option value="08">Temmuz</option>
                                        <option value="09">Ağustos</option>
                                        <option value="10">Eylül</option>
                                        <option value="11">Ekim</option>
                                        <option value="12">Kasım</option>
                                        <option value="13">Aralık</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                                <div class="yil">
                                    <label class="txt">&nbsp;</label>
                                    <select name="yillar" class="day">
                                        <option value="0">Yıl</option>
                                        <option value="01">Halen</option>
                                        <option value="02">2022</option>
                                        <option value="03">2021</option>
                                        <option value="04">2020</option>
                                        <option value="05">2019</option>
                                        <option value="06">2018</option>
                                        <option value="07">2017</option>
                                        <option value="08">2016</option>
                                        <option value="09">2015</option>
                                        <option value="10">2014</option>
                                        <option value="11">2013</option>
                                        <option value="12">2012</option>
                                        <option value="13">2011</option>
                                        <option value="14">2010</option>
                                        <option value="15">2009</option>
                                        <option value="16">2008</option>
                                        <option value="17">2007</option>
                                        <option value="18">2006</option>
                                        <option value="19">2005</option>
                                        <option value="20">2004</option>
                                        <option value="21">2003</option>
                                        <option value="22">2002</option>
                                        <option value="23">2001</option>
                                        <option value="24">2000</option>
                                        <option value="25">1999</option>
                                        <option value="26">1998</option>
                                        <option value="27">1997</option>
                                        <option value="28">1996</option>
                                        <option value="29">1995</option>
                                        <option value="30">1994</option>
                                        <option value="31">1993</option>
                                        <option value="32">1992</option>
                                        <option value="33">1991</option>
                                        <option value="34">1990</option>
                                        <option value="35">1989</option>
                                        <option value="36">1988</option>
                                        <option value="37">1987</option>
                                        <option value="38">1986</option>
                                        <option value="39">1985</option>
                                        <option value="40">1984</option>
                                        <option value="41">1983</option>
                                        <option value="42">1982</option>
                                        <option value="43">1981</option>
                                        <option value="44">1980</option>
                                        <option value="45">1979</option>
                                        <option value="46">1978</option>
                                        <option value="47">1977</option>
                                        <option value="48">1976</option>
                                        <option value="49">1975</option>
                                        <option value="50">1974</option>
                                        <option value="51">1973</option>
                                        <option value="52">1972</option>
                                    </select>
                                    <i class="ok"></i>
                                </div>
                            </div>
                        </div>
                        <div class="col1">
                            <textarea name="work" id="" cols="30" rows="10" placeholder="İş Deneyimi Hakkında"></textarea>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="button">
            <button class="deleteWork">
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="svg--deleteWork" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path>
                </svg>
            </button>
        </div>
    </li>
    `;
    work.innerHTML += html;
}

const generateSkill = () =>{
    const html = `
    <li>
        <div class="col1">
            <div>
                <div class="col3">
                    <label for="skill">Beceri</label>
                    <input type="text" name="skill" placeholder="ör. Microsoft Word">
                </div>
                <div class="col2">
                    <label for="level1">Düzey</label>
                    <select name="level1" id="" class="day">
                        <option value="0">Seç</option>
                        <option value="01">Uzman</option>
                        <option value="02">Deneyimli</option>
                        <option value="03">Yetenekli</option>
                        <option value="04">Başlangıç</option>
                        <option value="05">Acemi</option>
                    </select>
                    <i class="ok"></i>
                </div>
            </div>
        </div>
        <div class="button">
            <button class="deleteSkill">
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="svg--deleteSkill" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path>
                </svg>
            </button>
        </div>
    </li>
    `;
    skills.innerHTML += html;
}

const removeLanguage = e =>{
    if(e.target.classList.contains('deleteLang'))
    {
        e.target.parentElement.parentElement.remove();
    }
    else if(e.target.classList.contains('svg--deleteLang'))
    {
        e.target.parentElement.parentElement.parentElement.remove();
    }
}

const removeEducation = e =>{
    if(e.target.classList.contains('deleteEdu'))
    {
        e.target.parentElement.parentElement.remove();
    }
    else if(e.target.classList.contains('svg--deleteEdu'))
    {
        e.target.parentElement.parentElement.parentElement.remove();
    }
}

const removeWork = e =>{
    if(e.target.classList.contains('deleteWork'))
    {
        e.target.parentElement.parentElement.remove();
    }
    else if(e.target.classList.contains('svg--deleteWork'))
    {
        e.target.parentElement.parentElement.parentElement.remove();
    }
}

const removeSkill = e =>{
    if(e.target.classList.contains('deleteSkill'))
    {
        e.target.parentElement.parentElement.remove();
    }
    else if(e.target.classList.contains('svg--deleteSkill'))
    {
        e.target.parentElement.parentElement.parentElement.remove();
    }
}


addLang.addEventListener('click', ()=>{
    generateLanguage();
})

lang.addEventListener('click', e=>{
    e.stopPropagation();
    removeLanguage(e);
})

addEdu.addEventListener('click', ()=>{
    generateEducation();
})

edu.addEventListener('click', e=>{
    e.stopPropagation();
    removeEducation(e);
})

addWork.addEventListener('click', ()=>{
    generateWork();
})

work.addEventListener('click', e=>{
    e.stopPropagation();
    removeWork(e);
})

addSkill.addEventListener('click', ()=>{
    generateSkill();
})

skills.addEventListener('click', e=>{
    e.stopPropagation();
    removeSkill(e);
})