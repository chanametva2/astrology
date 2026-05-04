---
title: บันทึกวิกิ
summary: บันทึกตามลำดับเวลาของการตั้งค่า ingest update และ lint วิกิ
tags: [wiki, log]
sources: []
related:
  - title: วิกิ
    url: /wiki/
layout: wiki
---

## 2026-05-04

- คืนค่าเมนูและ theme locale เป็นภาษาอังกฤษตามต้องการ โดยคงเนื้อหา wiki เป็นภาษาไทย

- แก้ชื่อ related link ที่ยังเป็นอังกฤษ เช่น `Wiki Log` และ `Wiki Index` ให้เป็นภาษาไทย

- เพิ่ม `_includes/sidebar.html` override เพื่อให้ sidebar ใช้ชื่อเมนูจาก front matter ภาษาไทยและไม่บังคับ `upcase`

- เปลี่ยน `_config.yml` เป็น `lang: th` เพื่อให้เมนูและข้อความ theme ของ Chirpy ใช้ locale ภาษาไทย

- เพิ่ม `title` ภาษาไทยให้ tab มาตรฐานใน `_tabs/` เพื่อให้เมนู sidebar แสดงเป็นภาษาไทย

- แปลหน้า sidebar wiki, layout label, index และหน้าวิกิแนวคิดทั้งหมดเป็นภาษาไทย โดยคง URL เดิมและ schema เดิมไว้

- เพิ่ม `_tabs/wiki.md` เพื่อให้วิกิแสดงใน sidebar ของ Chirpy ที่ `/wiki/`
- ย้าย render path ของ `_wiki/index.md` ไปที่ `/wiki/index/` เพื่อเลี่ยง permalink conflict กับหน้า sidebar tab

- Batch-ingested 13 posts จาก `_posts/` และตรวจ asset ที่เกี่ยวข้องใน `assets/`
- สร้างหน้าแนวคิดสำหรับโหราศาสตร์ในฐานะภาษาสัญลักษณ์ การอ่านดวงกำเนิด ราศี ธาตุ modality ดาวเจ้าเรือน essential dignity ระบบให้น้ำหนัก และกรณีศึกษาดวง Donald Trump
- รวมคำอธิบายที่ซ้ำกันเรื่องธาตุ modality rulership dignity และระบบให้น้ำหนักไว้ในหน้าวิกิถาวร แทนการสรุปแยกตามบทความ
- อัปเดต `_wiki/index.md` หนึ่งครั้งด้วยกลุ่มแนวคิดและคงรายการหน้าแบบ dynamic ไว้
- ไม่ได้แก้ไฟล์ source posts หรือ asset

- ตั้งค่าชั้น wiki เป็น Jekyll collection ชื่อ `wiki` ที่ render ใต้ `/wiki/`
- เพิ่ม layout wiki ที่ใช้ซ้ำได้ หน้า index และบันทึกการดูแลตามลำดับเวลา
- เพิ่มกฎ maintenance, ingest และ lint ของ wiki ใน `AGENTS.md`
- ไม่ได้แก้ source posts หรือ raw source files
