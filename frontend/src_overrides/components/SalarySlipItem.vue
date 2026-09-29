<template>
	<ListItem>
		<template #left>
			<SalaryIcon class="h-5 w-5 text-[#D4AF37]" />
			<div class="flex flex-col items-start gap-1.5">
				<div class="text-base font-medium text-white">
					{{ title }}
				</div>
				<div v-if="doc?.gross_pay" class="text-xs font-normal text-slate-300">
					<span>
						{{
							__("{0}: {1}", [
								__("Gross Pay"),
								formatCurrency(doc.gross_pay, doc.currency),
							])
						}}
					</span>
					<span class="whitespace-pre"> &middot; </span>
				</div>
			</div>
		</template>
		<template #right>
			<span v-if="doc?.net_pay" class="text-[#D4AF37] font-semibold rounded text-base">
				{{ formatCurrency(doc.net_pay, doc.currency) }}
			</span>
			<FeatherIcon name="chevron-right" class="h-5 w-5 text-[#D4AF37]" />
		</template>
	</ListItem>
</template>

<script setup>
import { computed, inject } from "vue"
import { FeatherIcon } from "frappe-ui"

import ListItem from "@/components/ListItem.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"

import { formatCurrency } from "@/utils/formatters"

const dayjs = inject("$dayjs")

const props = defineProps({
	doc: {
		type: Object,
	},
})

const title = computed(() => {
	if (dayjs(props.doc.start_date).isSame(props.doc.end_date, "month")) {
		// monthly salary
		return dayjs(props.doc.start_date).format("MMM YYYY")
	} else {
		// quarterly, bimonthly, etc
		return `${dayjs(props.doc.start_date).format("MMM YYYY")} - ${dayjs(
			props.doc.end_date
		).format("MMM YYYY")}`
	}
})
</script>
