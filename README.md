# CRISP: самоигра Challenger--Reasoner на основе корпуса документов для дообучения больших языковых моделей в предметных областях

[![License](https://badgen.net/github/license/draiqw/crisp?color=green)](https://github.com/draiqw/crisp/blob/main/LICENSE)
[![GitHub Contributors](https://img.shields.io/github/contributors/draiqw/crisp)](https://github.com/draiqw/crisp/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues-closed/draiqw/crisp.svg?color=0088ff)](https://github.com/draiqw/crisp/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr-closed/draiqw/crisp.svg?color=7f29d6)](https://github.com/draiqw/crisp/pulls)

<table>
    <tr>
        <td align="left"> <b> Автор </b> </td>
        <td> Роман Акрамов </td>
    </tr>
    <tr>
        <td align="left"> <b> Научный руководитель </b> </td>
        <td> Роман Валерьевич Ищенок </td>
    </tr>
</table>

## Материалы

- [Статья](paper/main.tex)

## Описание проекта

CRISP (Corpus-grounded Challenger--Reasoner Self-Play) -- сквозная «фабрика данных», которая превращает набор PDF-документов предметной области в два артефакта: корпус для предобучения и QA-датасет, пригодный без изменений и для SFT, и для RL. Конвейер состоит из четырёх этапов: OCR, очистка и фильтрация корпуса, самоигра Challenger--Reasoner на основе корпуса с наградой, зависящей от дисперсии, и курирование вопросов многокритериальным LLM-судьёй. Конвейер применяется к трём русскоязычным STEM-областям: общим дисциплинам университетского уровня, линейной алгебре, теории вероятностей и математической статистике.

## Аннотация

TODO

## Цитирование

```BibTeX
@article{akramov2026crisp,
    title={CRISP: самоигра Challenger--Reasoner на основе корпуса документов для дообучения больших языковых моделей в предметных областях},
    author={Акрамов, Роман and Ищенок, Роман Валерьевич},
    year={2026}
}
```

## Лицензия

Проект распространяется по лицензии MIT, подробности в [LICENSE](LICENSE).
