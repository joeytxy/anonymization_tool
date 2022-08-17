# Anonymisation Tool 

An anonymisation tool which utilises NER packages such as flair, NLTK,spaCy and stanza to mask personal names (default). Other information such as NRIC, phone number etc can also be masked by giving corresponding input.

The tool was evaluated based on a self-modified version of the WikiNeural data that can be found [here](https://github.com/Babelscape/wikineural)

Citation: 

``` 
Tedeschi, S., Maiorca, V., Campolungo, N., Cecconi, F., & Navigli, R. (2021). WikiNEuRal: Combined Neural and Knowledge-based Silver Data Creation for Multilingual NER. In Findings of the Association for Computational Linguistics: EMNLP 2021 (pp. 2521–2533). Association for Computational Linguistics.
```

<details><summary>Preview of Raw Dataset </summary>
<p>

<img width="123" alt="image" src="https://user-images.githubusercontent.com/66881214/185170721-d0573eaf-3cb8-4525-8479-b6b8125ba5c0.png">

</p>
</details>

<details><summary>Preview of Modified Dataset </summary>
<p>

| Sentence                                                                                                                                  | Output                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|  Since then , only Terry Bradshaw in 147 games , Joe Montana in 139 games , and Tom Brady in 131 games have reached 100 wins more quickly |  Since then , only \[Name\] in 147 games , \[Name\] in 139 games , and \[Name\] in 131 games have reached 100 wins more quickly |
|  He was portrayed by Anthony Perkins in the 1960 version of Psycho directed by Alfred Hitchcock and the Psycho franchise                  |  He was portrayed by \[Name\] in the 1960 version of Psycho directed by \[Name\] and the Psycho franchise                       |

</p>
</details>

