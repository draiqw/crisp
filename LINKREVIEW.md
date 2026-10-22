# LinkReview

- Здесь собраны работы, полезные для статьи, сгруппированные по темам.
- Сейчас в таблице 16 работ, которые цитирует статья. По требованиям курса нужно не меньше 40 — таблица будет дополняться.

> [!NOTE]
> Таблица обновляется и не является финальной версией.

| Тема | Название | Год | Авторы | Статья | Код | Кратко |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| Self-play на корпусе | SPICE: Self-Play In Corpus Environments Improves Reasoning | 2025 | Liu et al. | [arXiv](https://arxiv.org/abs/2510.24684) | — | Базовая работа: Challenger видит документ и задаёт вопрос, Reasoner отвечает без документа; награда Challenger максимальна при 50% решаемости. CRISP переносит идею на русскоязычные предметные корпуса. |
| Self-play без данных | R-Zero: Self-Evolving Reasoning LLM from Zero Data | 2025 | Huang et al. | [arXiv](https://arxiv.org/abs/2508.05004) | [GitHub](https://github.com/Chengsong-Huang/R-Zero) | Пара Challenger–Solver генерирует задачи без внешних данных. Без опоры на корпус такая генерация замыкается на знаниях модели. |
| Self-play без данных | Absolute Zero: Reinforced Self-play Reasoning with Zero Data | 2025 | Zhao et al. | [arXiv](https://arxiv.org/abs/2505.03335) | [GitHub](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) | Модель сама предлагает и решает задачи с проверкой через исполнение кода. Пример self-play, ограниченного верифицируемыми доменами. |
| Синтетические инструкции | Self-Instruct: Aligning Language Models with Self-Generated Instructions | 2022 | Wang et al. | [arXiv](https://arxiv.org/abs/2212.10560) | [GitHub](https://github.com/yizhongw/self-instruct) | Генерация инструкций самой моделью из небольшого набора затравок. Базовый подход к синтетическим данным для дообучения. |
| Синтетические инструкции | WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions | 2023 | Xu et al. | [arXiv](https://arxiv.org/abs/2304.12244) | [GitHub](https://github.com/nlpxucan/WizardLM) | Evol-Instruct: итеративное усложнение инструкций с помощью LLM. |
| Синтетические инструкции | WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct | 2023 | Luo et al. | [arXiv](https://arxiv.org/abs/2308.09583) | [GitHub](https://github.com/nlpxucan/WizardLM) | Evol-Instruct для математики с подкреплением. Синтетика без привязки к корпусу предметной области. |
| RL для рассуждений | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | 2024 | Shao et al. | [arXiv](https://arxiv.org/abs/2402.03300) | — | Вводит GRPO — групповую относительную оптимизацию политики без критика, которую мы используем для обучения. |
| RL для рассуждений | Understanding R1-Zero-Like Training: A Critical Perspective | 2025 | Liu et al. | [arXiv](https://arxiv.org/abs/2503.20783) | [GitHub](https://github.com/sail-sg/understand-r1-zero) | Dr. GRPO: убирает смещения нормировки GRPO по длине и дисперсии. Используется как вариант оптимизации. |
| RL для рассуждений | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | 2025 | DeepSeek-AI | [arXiv](https://arxiv.org/abs/2501.12948) | — | Показывает, что RL с проверяемыми наградами развивает рассуждения LLM. Мотивация RLVR. |
| Инфраструктура RL | HybridFlow: A Flexible and Efficient RLHF Framework | 2024 | Sheng et al. | [arXiv](https://arxiv.org/abs/2409.19256) | [GitHub](https://github.com/volcengine/verl) | Фреймворк verl, на котором выполнено downstream GRPO-дообучение. |
| Данные для предобучения | The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale | 2024 | Penedo et al. | [arXiv](https://arxiv.org/abs/2406.17557) | — | Открытый веб-корпус с фильтрацией по качеству. Эталон для сравнения нашего корпуса и пример LLM-фильтрации. |
| OCR | Chandra: OCR model for converting documents to Markdown | 2025 | Datalab | — | [GitHub](https://github.com/datalab-to/chandra) | VLM-модель OCR, которой PDF-учебники переводятся в Markdown на первом этапе конвейера. |
| Проверка ответов | Math-Verify: a robust mathematical expression evaluation system | 2025 | Hugging Face | — | [GitHub](https://github.com/huggingface/Math-Verify) | Проверка эквивалентности математических ответов, используется для бинарной награды Reasoner. |
| Бенчмарки | Training Verifiers to Solve Math Word Problems | 2021 | Cobbe et al. | [arXiv](https://arxiv.org/abs/2110.14168) | [GitHub](https://github.com/openai/grade-school-math) | Датасет GSM8K, школьные текстовые задачи. Публичный бейзлайн и бенчмарк. |
| Бенчмарки | Measuring Mathematical Problem Solving With the MATH Dataset | 2021 | Hendrycks et al. | [arXiv](https://arxiv.org/abs/2103.03874) | [GitHub](https://github.com/hendrycks/math) | Датасет MATH, олимпиадные задачи. Используется подмножество MATH-500 для оценки. |
| Бенчмарки | LinAlg-Bench: A Forensic Benchmark Revealing Structural Failure Modes in LLM Mathematical Reasoning | 2026 | Agarwal et al. | [arXiv](https://arxiv.org/abs/2605.16675) | — | Бенчмарк по линейной алгебре для оценки в узкой предметной области. |
