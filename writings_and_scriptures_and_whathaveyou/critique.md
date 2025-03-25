Some Questions:
- What is the purpose of this visualization? How has the designer tailored this visualization to
meet particular user information needs or goals?

  This visualization is designed to show how NBA shot selection has changed over time. It presents shot location data from alternating seasons between 1997 and 2020, making it easy to spot trends like the growing reliance on three-pointers and the decline of mid-range shots. The layout helps users compare different years side by side, making the evolution of the game clear.

- Does this visualization require training/study to work, or is it immediately effective?

  It is very easy to understand at a glance. The dots on the court naturally represent shot locations, so anyone familiar with basketball can quickly grasp what is being shown. There is no need for special training or a legend to figure it out.

- How are the data encoded into visual form? Does the author use specific visual channels
(in)effectively to represent certain dimensions?

  - The position of the dots on the court directly maps to where players take shots

  - The orange hexagons highlight the most frequent shooting spots

  - The grid layout (small multiples) makes it easy to compare different years at a glance

  The visual choices work well, but one limitation is that it only shows shot frequency and not accuracy. This means we do not know whether these were high-quality shots or just commonly attempted ones. Additionally, we don't get insight into the frequency of shots beyond the number being beyond some unstated threshold.

- What design trade-offs are present in the visualization? Are they emphasizing some part of the
data at the expense of something else?

  - The focus is on shot volume rather than efficiency. This makes it great for showing where players shoot from, but it does not tell us whether those shots were successful. Some viewers might assume the most frequent shots are also the best ones, which is not necessarily true

  - Some areas of the court get dense with hexagons, making it harder to see changes from year to year

- How is interaction employed in this visualization? Are there any trade-offs that come from
introducing interactions? Are the interactions helpful?

  This is a static visualization, meaning there is no way to interact with the data. Adding interactivity, such as hover effects to display shooting percentages, filters for different player positions, or animations to transition between years, could make it even more insightful.

- Do you feel that this visualization is successful? What elements help make it effective, and what
hurt its effectiveness?

  Yes, overall, it effectively shows shot trends over time.

  What works well:

  - Clear and easy-to-read shot distributions

  - Highlights major trends like the rise of three-pointers

  - The year-by-year layout makes changes easy to spot

What could be better:

  - It does not show shot accuracy, which is a key missing element

  - There is no differentiation between types of players. Guards and big men likely have very different shooting habits, but that is not visible here

  - Some added context, like rule changes, would help explain why certain trends happened

- What’s missing from the visualization that would improve it? Is any element of the visualization
misleading or at risk of misinterpretation?

  - There is no shot success data. Seeing whether these shots were efficient would make the visualization much more valuable

  - There is no breakdown of player types. Are these shots coming from superstars, role players, or a mix? That information would add more depth

  - There are no annotations or explanations. Major rule changes, like the introduction of new defensive rules or the rise of analytics-driven strategies, could help explain why certain patterns emerged