---
date: '2022-10-03T19:26:38+08:00'
aliases: ["Practice Autofocus Method in Todoist"]
feature: "featured-river-flowing-with-maple-leaves-on-the-rocks.jpg"
banner: "![[featured-river-flowing-with-maple-leaves-on-the-rocks.jpg]]"
banner_y: 0.54093
---
# Practice Autofocus Method in Todoist

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2022-10-03]]
**Reference**:: [[Brett McKay et al. - Autofocus The Productivity System That Treats Your to-Do List Like a River (Highlights)]]

I read the article *Autofocus: The Productivity System That Treats Your to-Do List Like a River*[[#^ref-1]] recently. I used to fill the time slots with tasks daily, but I rarely completed all the planned tasks. Even for the completed ones, I often missed the scheduled time slot. I felt stressed and guilty. So I decide to give the Autofocus Method a try.

<!--more-->

## The River Filter

I will continue using Todoist. I created a filter named *River*. The tasks are sorted by added date. I added the filter to the sidebar and set it as my home view for easy access.

The filter has three sections:

- Overdue tasks: `overdue`
- Tasks I am doing: `today | @now💧`
- Tasks in River: `!##⏰ Events & !overdue & !today & !@now💧 & !@someday🪨`

Todoist supports filter sections by separating queries with comma (`,`). So here is the final filter query:

```
overdue, today | @now💧, !##⏰ Events & !overdue & !today & !@now💧 & !@someday🪨
```

### Section 1: Overdue Tasks

This section allows me to re-schedule the overdue tasks.

I decided to not totally abandon the due dates. However, I use them with great moderation. I set a due date if I must complete the task on that date, and before the day comes, I can forget the task.

I add such tasks to the project `⏰ Events`. They will appear in the River filter when they are due or overdue.

### Section 2: Tasks I Am Doing

This section lists tasks that I am doing now.

There are two kinds of such tasks.

The first is the scheduled tasks that are due today.

The second is the selected tasks from the river. I add the tag `@now💧` to the task if I feel like doing it.

### Section 3: Tasks in River

This section contains the tasks in the river. It excludes tasks from the project `⏰ Events`, and the dismissed tasks. I tag dismissed tasks with `@someday🪨` .

## The Workflow

I add new tasks to the inbox without triaging the projects, tags, due dates, and priorities. Since the filter

When I have time to do something, I open the River filter and scan the tasks from top to bottom without scrolling down.

First, I re-schedule the overdue tasks.

Then, I do a quick scan on the second section—the tasks that I planned before. If I feel like doing a task in the list, I start working on it.

If I failed to find a task to work on in the previous step, I continue the scan to the last section—the tasks in the river. I add tag `@now💧` to pop the task to the top of the list.

If there are no items stands out for me, I have three choices to remove tasks from the first screen:

- Defer the scheduled tasks into future.
- Remove the tag `@now💧` from the task.
- Dismiss a task by adding the tag `@someday🪨`.

The Autofocus Method suggests to cross the item off the list and re-enter it at the end of the list if I haven't finished it yet. In Todoist, I duplicate the task and cross the original item off.

Here is my setup to practice the Autofocus Method in Todoist. I'm still experimenting to see whether it can improve my productivity.

## References

1. McKay, B., & McKay, K. (2022, September 20). *Autofocus: The Productivity System That Treats Your To-Do List Like a River*. The Art of Manliness. <https://www.artofmanliness.com/character/behavior/autofocus-the-productivity-system-that-treats-your-to-do-list-like-a-river/> ^ref-1