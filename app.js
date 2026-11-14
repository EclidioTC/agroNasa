const API_URL = "http://127.0.0.1:5000/previsao";
const REGIAO_DEMO = "Chokwe";
const DATA_DEMO = "2026-11-14";

let lang = "pt"; 
let frases = null;
let contratoFallback = null;
let dadosAtuais = null; // Variável para guardar os dados do servidor

const content = document.getElementById("content");
const audioEl = document.getElementById("ivr");

async function init() {
  try {
    const r1 = await fetch("frases_validadas.json");
    frases = await r1.json();
  } catch (e) { frases = { pt: {}, xh: {} }; }

  try {
    const r2 = await fetch("contrato_oficial.json");
    contratoFallback = await r2.json();
  } catch (e) { contratoFallback = null; }

  renderMenu();
}

function t(chave) {
  const l = lang || "pt";
  const v = (frases[l] && frases[l][chave]) ? frases[l][chave] : "";
  if (v && v.trim() !== "") return v;
  return (frases.pt && frases.pt[chave]) ? frases.pt[chave] : `[${chave}]`;
}

function render(html) { content.innerHTML = html; }

function renderMenu() {
  render(t("menu") + '<input id="input" maxlength="2" inputmode="numeric">');
  focusInput();
}

function renderMenuIdioma() {
  render(t("menuIdioma") + '<input id="input" maxlength="1" inputmode="numeric">');
  focusInput();
}

function focusInput() {
  const i = document.getElementById("input");
  if (i) { i.focus(); i.addEventListener("keydown", e => { if (e.key === "Enter") submeter(i.value); }); }
}

function press(tecla) {
  if (tecla === "*") { 
    renderMenu(); 
    return; 
  }

  const input = document.getElementById("input");
  if (!input) return; 
  
  if (tecla === "#") { 
    submeter(input.value); 
    input.value = ""; 
  } else { 
    input.value += tecla; 
  }
}

function submeter(valor) {
  if (lang === "menu_idioma") {
    if (valor === "1" || valor === "2") {
      const idioma = (valor === "1") ? "pt" : "xh";
      const estado = dadosAtuais || contratoFallback || { cenario: "seca", nivel: "vermelho" };
      
      lang = "pt"; 
      tocarIVR(estado.cenario, estado.nivel, idioma); 
    } else {
      lang = "pt";
      renderMenu(); 
    }
    return;
  }

  if (valor === "1") consultar("alerta");
  else if (valor === "2") consultar("culturas");
  else if (valor === "3") { 
    lang = "menu_idioma"; 
    renderMenuIdioma(); 
  }
  else if (valor === "4") { render(t("obrigado")); setTimeout(() => { renderMenu(); }, 1500); }
  else renderMenu();
}

async function consultar(tipo) {
  render(t("aCarregar"));
  let dados = null;
  try {
    const resp = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ regiao: REGIAO_DEMO, data: DATA_DEMO })
    });
    if (!resp.ok) throw new Error("HTTP " + resp.status);
    dados = await resp.json();
  } catch (e) {
    dados = contratoFallback;
  }

  dadosAtuais = dados; // GUARDA OS DADOS PARA O ÁUDIO

  if (!dados) { render(t("erro")); setTimeout(renderMenu, 2000); return; }
  if (tipo === "alerta") render(formatarAlerta(dados));
  else render(formatarCulturas(dados));
}

function formatarAlerta(d) {
  const nivelKey = { verde: "nivelVerde", amarelo: "nivelAmarelo", vermelho: "nivelVermelho" }[d.nivel] || "nivelVermelho";
  const nivelTxt = t(nivelKey);
  const prob = Math.round(d.probabilidade * 100);
  const comp = d.compensacao > 0 ? `<br>${t("compensacao")}: ${d.compensacao} MT` : "";
  return `${t("alertaPrefixo")}: ${nivelTxt}<br>
    ${d.cenario.toUpperCase()} — ${d.regiao}<br>
    Prob: ${prob}%${comp}<br><br>
    <i>${t("voltar")}</i>`;
}

function formatarCulturas(d) {
  const rec = d.culturas_recomendadas.slice(0, 3).join(", ");
  const ev = d.culturas_a_evitar.join(", ");
  return `✅ ${t("plantar")}:<br>${rec}<br><br>
    ⚠️ ${t("evitar")}:<br>${ev}<br><br>
    <i>${t("voltar")}</i>`;
}

function tocarIVR(cenario, nivel, idioma) {
  let nomeFicheiro = `${cenario}_${nivel}`;
  
  if (cenario === "normal" && nivel === "verde") {
      nomeFicheiro = "alerta_verde";
  }

  if (idioma === "xh") {
      nomeFicheiro += "_xh"; 
  }

  const ficheiro = `audio/${nomeFicheiro}.mp3`;
  
  audioEl.src = ficheiro;
  audioEl.play().catch(() => {
    const aviso = idioma === "xh" ? "Áudio em Changana indisponível." : "Áudio em Português indisponível.";
    render(`⚠️ ${aviso}<br><br><i>${t("voltar")}</i>`);
    setTimeout(renderMenu, 3000);
  });
  
  const textoIdioma = idioma === "xh" ? "Changana" : "Português";
  render(`🔊 A reproduzir áudio em ${textoIdioma}...<br><br><i>${t("voltar")}</i>`);
  setTimeout(renderMenu, 15000); 
}

init();