---
title: Wiki
layout: wiki
icon: fas fa-book
order: 5
permalink: /wiki/
summary: จุดเริ่มต้นของฐานความรู้โหราศาสตร์แบบถาวรในเว็บไซต์นี้
tags: [wiki, index]
sources: []
related:
  - title: บันทึกวิกิ
    url: /wiki/log/
---

วิกินี้คือชั้นความรู้ที่ดูแลต่อเนื่องของเว็บไซต์ บทความในบล็อกยังเป็นแหล่งข้อมูลตามลำดับเวลา ส่วนหน้าวิกิสรุปแนวคิด บุคคล ระบบ และหัวข้อที่ควรเก็บไว้ใช้ระยะยาว

## กลุ่มแนวคิด

- [โหราศาสตร์ในฐานะภาษาสัญลักษณ์]({{ '/wiki/astrology-as-symbolic-language/' | relative_url }}): กรอบการอ่านรูปแบบ แนวโน้ม จังหวะเวลา และความหมาย
- [การอ่านดวงกำเนิด]({{ '/wiki/natal-chart-reading/' | relative_url }}): ลำดับการอ่านดวงทั้งผืนและข้อควรระวัง
- [ราศีจักรราศี]({{ '/wiki/zodiac-signs/' | relative_url }}): ฐานเชิงฤดูกาล สัญลักษณ์ และโครงสร้างของ 12 ราศี
- [ธาตุ]({{ '/wiki/elements/' | relative_url }}): ไฟ ดิน ลม น้ำ ในฐานะชนิดพื้นฐานของพลัง
- [Modality]({{ '/wiki/modality/' | relative_url }}): จังหวะพลังแบบ cardinal, fixed และ mutable
- [ดาวเจ้าเรือนของราศี]({{ '/wiki/sign-rulership/' | relative_url }}): ระบบ ruler แบบดั้งเดิมและความสมมาตรของระบบ
- [Essential Dignity]({{ '/wiki/essential-dignity/' | relative_url }}): domicile, detriment, exaltation และ fall
- [ระบบให้น้ำหนักในดวงชะตา]({{ '/wiki/weighted-chart-scoring/' | relative_url }}): วิธีให้คะแนนเพื่อดูน้ำหนักของพลังในดวง
- [กรณีศึกษาดวง Donald Trump]({{ '/wiki/donald-trump-chart-case-study/' | relative_url }}): ตัวอย่างการใช้ธาตุและ modality แบบให้น้ำหนัก

## หน้าวิกิทั้งหมด

{% assign wiki_pages = site.wiki | where_exp: "page", "page.url != '/wiki/index/'" | sort: "title" %}
{% for wiki_page in wiki_pages %}
- [{{ wiki_page.title }}]({{ wiki_page.url | relative_url }}){% if wiki_page.summary %}: {{ wiki_page.summary }}{% endif %}
{% endfor %}

## การดูแลวิกิ

- [บันทึกวิกิ]({{ '/wiki/log/' | relative_url }}): บันทึกตามลำดับเวลาของการ ingest, update และ lint วิกิ

## กติกาการใช้งาน

- ห้ามแก้แหล่งข้อมูลดิบ เว้นแต่มีคำสั่งชัดเจน
- หน้าวิกิเป็นสรุปหัวข้อถาวร ไม่ใช่บทความตามลำดับเวลา
- ควรอัปเดตหน้าที่มีอยู่ก่อนสร้างหน้าใหม่
- ทุกครั้งที่ ingest, update หรือ lint ต้องอัปเดต index และเพิ่มบันทึกใน log
