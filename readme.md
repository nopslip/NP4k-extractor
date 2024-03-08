# NP4K Extractor --> Fabric 

## Purpose 
This is a simple script that takes a list of URLs for blog posts, articles, etc and runs [Newspaper4K](https://github.com/AndyTheFactory/newspaper4k) against them to extract summaries, keywords, titles, and other metadata fields. It can also use NLP to assess sentiment.  

It was created to extract data and feed it into [Fabric](https://github.com/danielmiessler/fabric) for generating summaries, extracting wisdom, or lesson plans and objectives. Or any other Fabric patterns that make sense. 

## Setup

1. You should probably run this script in a Python virtual env. It was created using 3.11.7. 
2. Install NP4K: `pip install newspaper4k`
3. While you can use the script to just extract data from URLs it's more fun to feed the data to [Fabric](https://github.com/danielmiessler/fabric) so you should install that. 

## Usage 

1. Create a list

First, create a file with your list of URLs that point to blog posts or articles on a given topic. See [sample.list.txt](sample.list.txt) as an example. 

2. Then run the script:

```
python extract_articles.py --file sample.list.txt
```

output: 
```ZMBPM1➜  extractor  ᐅ  python extract_articles.py --file sample.list.txt 
2024-03-08 13:36:23,271 - __main__ - INFO - Found 5 URLs to process!
2024-03-08 13:36:23,271 - __main__ - INFO - Processing URL: https://consumer.ftc.gov/articles/what-know-about-romance-scams
2024-03-08 13:36:27,686 - __main__ - INFO - Processing URL: https://clario.co/blog/romance-scams
2024-03-08 13:36:31,936 - __main__ - INFO - Processing URL: https://www.consumerfinance.gov/about-us/blog/break-up-with-online-romance-scams/
2024-03-08 13:36:33,282 - __main__ - INFO - Processing URL: https://www.aarp.org/money/scams-fraud/info-2019/romance.html
2024-03-08 13:36:34,502 - __main__ - INFO - Processing URL: https://www.ice.gov/features/LoveOnline
2024-03-08 13:36:38,637 - __main__ - INFO - Successfully wrote extracted data to _output_sample.list.txt_1709930183.txt
```

The script will output a file like [_output_sample.list.txt_1709930183.txt](_output_sample.list.txt_1709930183.txt) or you can use `--format JSON` to get [JSON](_output_sample.list.txt_1709925366.json). 

4. Feed Fabric 

Then you can feed the output directly to Fabric. By default, it's extracting a lot of metadata from the articles. You should only send what you need into Fabric(-->OpenAI) to keep costs down. So, let's say you only want to send the text and title: 

```
grep -E '^(title|text):' _output_sample.list.txt_1709930183.txt | fabric --pattern extract_wisdom > fabric_output_sample.list.txt_1709930183.txt
```

This command extracts the title and text from our output file, feeds it to Fabric extract_wisdom, and then write the results to the file [fabric_output_sample.list.txt_1709930183.txt](fabric_output_sample.list.txt_1709930183.txt). 


It would be cool if Fabric had some concept of a pre-processor or plugin so scripts like this could be integrated as a first-class component but of course, it's also really easy to just run it independently and pipe the results in too. 

I used this method to help craft a lesson on [how to avoid Romance Scams](https://blueox.ai/course/lesson/romance-scams-unmasked/). 

FABRIC OUTPUT: 

## SUMMARY

The content discusses the phenomenon of romance scams, where fraudsters create fake profiles on dating sites, social media, and apps to trick individuals into sending them money by pretending to be in a romantic relationship. It covers various tactics used by scammers, the significant financial losses victims have incurred, and provides advice on how to avoid falling prey to these scams. It also includes personal stories, statistics from the Federal Trade Commission (FTC), and tips on reporting and protecting oneself from such scams.

## IDEAS:

- Romance scams involve fraudsters pretending to be interested in a romantic relationship to trick victims into sending money.
- Scammers often create fake profiles on dating sites and social media platforms.
- Victims have reported losing significant amounts of money, with losses increasing annually.
- Scammers use various tactics, including pretending to need money for emergencies, plane tickets, or medical expenses.
- Gift cards and cryptocurrency are common payment methods requested by scammers.
- Performing a reverse image search on profile pictures can help identify fake profiles.
- The FTC and other organizations provide resources for reporting romance scams.
- Older adults are particularly vulnerable to romance scams, with losses amounting to millions annually.
- Scammers target victims through direct messages, friend requests, and emails.
- Romance scams can evolve into other forms of fraud, such as money laundering or cryptocurrency investment scams.
- The emotional impact of romance scams can be devastating for victims.
- Awareness and education are key to preventing romance scams.
- Limiting personal information shared online can help protect against scammers.
- Being skeptical of too-good-to-be-true love interests and refusing to send money are crucial prevention steps.
- Romance scams have become more sophisticated, using tactics like catfishing and blackmail.
- Scammers often claim to be working overseas in professions like the military or oil rigs to explain their inability to meet in person.
- The rise of online dating has led to an increase in romance scams.
- Social isolation, such as that experienced during the COVID-19 pandemic, has made individuals more susceptible to romance scams.
- Law enforcement agencies work together to combat and prosecute those behind romance scams.

## QUOTES:

- "People reported a record $547 million in losses to romance scams in 2021."
- "Never send money or gifts to a sweetheart you haven’t met in person."
- "Romance scammers create fake profiles on dating sites and apps."
- "The older the target, the heavier the financial toll."
- "Scammers use pictures of an attractive person...to lure someone into a romantic relationship."
- "Loneliness — especially during COVID-19 isolation periods — and the development of new technologies have contributed to the continued rise of romance scams."
- "Older adults reportedly lost nearly $139 million in romance scams in 2020."
- "Be suspicious if you haven’t met in person."
- "Don’t overshare personal information."
- "Think you’ve been scammed? Stop communicating with the individual immediately."

## HABITS:

- Regularly updating online dating profiles to reflect accurate information.
- Conducting reverse image searches on profile pictures of new online acquaintances.
- Limiting the amount of personal information shared on social media and dating sites.
- Engaging in conversations with new online connections cautiously and skeptically.
- Asking detailed questions when communicating with potential romantic interests online.
- Verifying the stories and backgrounds of online love interests through independent research.
- Discussing new online romantic interests with friends or family for a second opinion.
- Reporting suspected romance scammers to the FTC and other relevant platforms.
- Using reputable and well-established dating websites only.
- Trusting gut instincts when interacting with potential romantic partners online.

## FACTS:

- In 2021, people reported paying romance scammers more with gift cards than with any other payment method.
- Almost 70,000 people in the US reported romance scams in 2022, resulting in around $1.3 billion in losses.
- The median individual loss from a romance scam for people 70 and over was $9,000 in 2021.
- Older adults turning to the internet for dating has doubled over the past three years.
- The Federal Trade Commission received some 56,000 complaints about romance scams in 2021.
- Romance scams are riskiest to people in the 55 – 64 age group.
- Criminal organizations involved in romance scams often originate in West Africa, predominantly Nigeria and Ghana.
- The US Army has published a fact sheet on how to spot and avoid scammers claiming to be American soldiers.

## REFERENCES:

- Federal Trade Commission (FTC) reports on romance scams
- Social Catfish’s list of the top 100 photos used for catfishing
- Homeland Security Investigations' advice on avoiding romance scams
- Clario AntiSpy’s web extension for safe browsing
- US Army's fact sheet on military romance scams

## RECOMMENDATIONS:

- Perform reverse image searches on profile pictures of new online acquaintances.
- Limit personal information shared on social media and dating platforms.
- Be skeptical of too-good-to-be-true love interests who ask for money.
- Use reputable and well-established dating websites only.
- Report suspected romance scammers to the FTC and other relevant platforms.
- Discuss new online romantic interests with friends or family for a second opinion.
- Trust your gut instincts when interacting with potential romantic partners online.
- Consider making social media profiles private to protect against scammers.
- Research the individual’s photo and profile using online searches for inconsistencies.
- Never send money to anyone you have only communicated with online or by phone.



