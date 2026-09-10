# UGC Product Review Skill

Bản tiếng Việt của README. Tài liệu chính và ví dụ kỹ thuật được duy trì bằng tiếng Anh để dễ dùng trong cộng đồng Agent Skills.

Đây là một **Agent Skill dạng modular** giúp AI tự phân tích sản phẩm và tạo video review UGC realistic: chọn concept, hook, hero moment, shot sequence, giữ consistency của creator và sản phẩm, thêm ràng buộc vật lý theo category, QA video generate và repair prompt.

## Cài đặt nhanh

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review
```

Cài global:

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review -g
```

Ví dụ cho Claude Code hoặc Codex:

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review -a claude-code
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review -a codex
```

## Cách sử dụng

Chỉ cần đưa ảnh hoặc thông tin sản phẩm và yêu cầu:

```text
Create a realistic 12-second UGC review video for this product.
```

Skill sẽ chủ động:

1. xác định loại sản phẩm,
2. tìm visual proof mạnh nhất,
3. xác định buyer motivation hoặc objection,
4. chọn dạng video phù hợp,
5. tạo hook, first frame, emotional arc và hero moment,
6. xây shot sequence có tính vật lý hợp lý,
7. tạo prompt production-ready,
8. đề xuất các góc video khác nhau.

## Kiến trúc

Skill sử dụng **progressive disclosure**. `SKILL.md` chỉ đóng vai trò router, còn các module chi tiết chỉ được nạp khi cần.

Ví dụ một video đơn chỉ cần:

```text
core
+ creative strategy
+ một category phù hợp
+ prompt compiler
```

QA, campaign, performance learning, model adapters và commercial claims không được load nếu không liên quan.

## Đóng góp

Repo được thiết kế để dễ contribution. Các dạng PR phù hợp gồm:

- thêm một product category mới,
- bổ sung một lỗi generate thực tế và cách repair,
- cải thiện physics/hand interaction của một category,
- thêm compatibility note cho coding agent,
- thêm campaign example,
- cải thiện validator.

Xem `CONTRIBUTING.md` và `docs/ROADMAP.md`.

## Nguyên tắc

- Visual proof > marketing claims
- Product fidelity > cinematic complexity
- Physical plausibility > spectacle
- Human imperfection > commercial polish

README chính: [README.md](README.md)
