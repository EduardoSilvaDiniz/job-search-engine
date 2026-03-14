import asyncio
import json
import os

from playwright.async_api import async_playwright
from playwright_stealth import Stealth


async def realizar_buscas(pesquisa: str):
    stealth = Stealth()

    async with async_playwright() as p:
        print("Iniciando script com nova sintaxe Stealth...")
        user_data_dir = os.path.join(os.getcwd(), "profiles/perfil_indeed")

        context = await p.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            no_viewport=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        )


        await = stealth.apply_stealth_async(context)

        page = context.pages[0]

        url = f"https://br.indeed.com/jobs?q={pesquisa}&l=Estado+de+S%C3%A3o+Paulo"
        await page.pause()
        print(f"Acessando: {url}")

        # await page.goto(url, wait_until="domcontentloaded")

        # # Verificação de Cloudflare
        # if "Verify you are human" in await page.content():
        #     print("\n🚨 CLOUDFLARE DETECTADO! Resolva manualmente e aperte ENTER...")
        #     input()

        # try:
        #     await page.wait_for_selector(".job_seen_beacon", timeout=10000)
        # except:
        #     print("Cards não encontrados.")
        #     await context.close()
        #     return

        # cards = page.locator(".job_seen_beacon")
        # total_vagas = await cards.count()
        # print(f"Foram encontradas {total_vagas} vagas.\n")

        # resultados_bronze = []

        # for i in range(total_vagas):
        #     try:
        #         card = cards.nth(i)
        #         await card.click()
        #         await page.wait_for_timeout(2500)

        #         # Extração Camada Bronze
        #         cargo = await card.locator('h2 span[id^="jobTitle"]').first.inner_text()
        #         empresa = await card.locator('[data-testid="company-name"]').first.inner_text()

        #         vaga_data = {
        #             "id": i + 1,
        #             "cargo": cargo,
        #             "empresa": empresa,
        #             "tipo_vaga": await page.locator('.js-match-insights-provider-1tasxgl li').all_inner_texts(),
        #             "descricao_completa": await page.locator('#jobDescriptionText').inner_text() if await page.locator('#jobDescriptionText').count() > 0 else "",
        #             "topicos_chave": await page.locator('#jobDescriptionText b, #jobDescriptionText strong').all_inner_texts(),
        #             "data_extracao": "2026-03-13" # Adicionando um metadado bronze
        #         }

        #         print(f"✅ Extraído: {cargo}")
        #         resultados_bronze.append(vaga_data)

        #     except Exception as e:
        #         print(f"❌ Erro na vaga {i+1}")
        #         continue

        # # Salva o arquivo Bronze
        # with open("vagas_bronze.json", "w", encoding="utf-8") as f:
        #     json.dump(resultados_bronze, f, ensure_ascii=False, indent=4)

        # print("\nPronto! JSON gerado.")
        await context.close()


if __name__ == "__main__":
    asyncio.run(realizar_buscas("estagio+ti"))
