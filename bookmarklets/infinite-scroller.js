javascript:(function(){async function scrollWithDelay(){for(let i=0;i<80;i++){await new Promise(resolve=>setTimeout(resolve,1500));window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});console.log(`Scroll ${i+1}/45`);}}scrollWithDelay();})();
