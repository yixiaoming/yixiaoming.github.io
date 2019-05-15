---
layout: page
title: 设计模式系列
show_title: false
permalink: /design_patterns.html
articles:
  data_source: site.categories.design_patterns
  type: brief
  show_info: true
---

<br/>
*设计模式真的是学了忘，忘了又学，是一个不断实践运用的过程，所以写这个设计模式系列，目的是为了记下一些常用的概念以及设计模式的使用方法和用途，以便下一次使用的时候能立即回忆起来，让它刻在脑袋里。*

<div>
{%- assign _page_articles_data_source = page.articles.data_source | default: layout.articles.data_source -%}

{%- if _page_articles_data_source -%}
{%- assign _keys = _page_articles_data_source | split: '.' -%}
{%- endif -%}

{%- assign _articles = nil -%}
{%- for _key in _keys -%}
  {%- if forloop.first -%}
    {%- case _key -%}
      {%- when 'site' -%}
        {%- assign _articles = site -%}
      {%- when 'page' -%}
        {%- assign _articles = page -%}
      {%- when 'layout' -%}
        {%- assign _articles = layout -%}
      {%- when 'paginator' -%}
        {%- assign _articles = paginator -%}
      {%- else -%}
        {%- assign _articles = site[_key] -%}
      {%- else -%}
    {%- endcase -%}
  {%- else -%}
    {%- assign _articles = _articles[_key] -%}
  {%- endif -%}
{%- endfor -%}

{%- assign _type = page.articles.type | default: layout.articles.type -%}

{%- if _articles -%}

  <div class="layout--articles">

    {%- if _type == 'grid' -%}
      {%- if page.articles.size == 'sm' -%}
        {%- include article-list.html articles=_articles type='grid' size='sm' -%}
      {%- else -%}
        {%- include article-list.html articles=_articles type='grid' -%}
      {%- endif -%}

    {%- elsif _type == 'brief' -%}
      {%- include snippets/assign.html
        target=site.data.variables.default.page.articles.show_info
        source0=layout.articles.show_info source1=page.articles.show_info -%}
      {%- assign _show_info = __return -%}

      {%- include article-list.html articles=_articles type='brief' show_info=_show_info -%}

    {%- else -%}
      {%- include snippets/assign.html
        target=site.data.variables.default.page.articles.show_cover
        source0=layout.articles.show_cover source1=page.articles.show_cover -%}
      {%- assign _show_cover = __return -%}

      {%- include snippets/assign.html
        target=site.data.variables.default.page.articles.show_excerpt
        source0=layout.articles.show_excerpt source1=page.articles.show_excerpt -%}
      {%- assign _show_excerpt = __return -%}

      {%- include snippets/assign.html
        target=site.data.variables.default.page.articles.show_readmore
        source0=layout.articles.show_readmore source1=page.articles.show_readmore -%}
      {%- assign _show_readmore = __return -%}

      {%- include snippets/assign.html
        target=site.data.variables.default.page.articles.show_info
        source0=layout.articles.show_info source1=page.articles.show_info -%}
      {%- assign _show_info = __return -%}

      {%- assign _article_type = page.articles.article_type | default: layout.articles.article_type -%}
      {%- assign _cover_size = page.articles.cover_size | default: layout.articles.cover_size -%}
      {%- assign _excerpt_type = page.articles.excerpt_type | default: layout.articles.excerpt_type -%}

      {%- include article-list.html articles=_articles type='item'
        article_type=_article_type
        show_cover=_show_cover cover_size=_cover_size
        show_excerpt=_show_excerpt excerpt_type=_excerpt_type
        show_readmore=_show_readmore show_info=_show_info -%}

    {%- endif -%}

  </div>
{%- endif -%}
</div>