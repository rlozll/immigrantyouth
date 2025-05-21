from django.shortcuts import render
from .models import Institution

def index(request):
    all_institutions = Institution.objects.all()

    institution_data = {}
    for inst in all_institutions:
        region = inst.region
        if region not in institution_data:
            institution_data[region] = []
        institution_data[region].append({
            'name': inst.name,
            'type': inst.type,
            'address': inst.address,
            'phone': inst.phone,
            'website': inst.website,
        })

    # 원하는 지역 순서
    region_order = ['서울', '경기', '인천', '세종', '충남', '경북', '울산', '경남', '부산']

    # 순서대로 정렬된 리스트 생성 (없는 지역은 빈 리스트로)
    sorted_institution_data = [(region, institution_data.get(region, [])) for region in region_order]

    return render(request, 'info/info.html', {'institution_data': sorted_institution_data})
