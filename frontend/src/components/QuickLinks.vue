<template>
	<div class="flex flex-col gap-3 my-2 w-full">
		<div class="flex items-center justify-between px-1">
			<h3 class="text-base sm:text-lg font-bold text-slate-900 tracking-tight">
				{{ title || __("Quick Links") }}
			</h3>
			<span class="text-xs text-slate-400 font-medium">Frequent Services</span>
		</div>
		<div class="flex flex-col bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden divide-y divide-slate-100">
			<router-link
				class="flex flex-row items-center justify-between p-3.5 sm:p-4 hover:bg-slate-50/80 active:bg-slate-100 transition group"
				v-for="(link, idx) in props.items"
				:key="link.title"
				:to="{ name: link.route }"
			>
				<div class="flex flex-row items-center gap-3.5 grow">
					<div 
						class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0 transition-transform group-hover:scale-105"
						:class="getIconBadgeClass(link.title, idx)"
					>
						<component :is="link.icon" class="h-5 w-5" />
					</div>
					<div class="text-sm sm:text-base font-medium text-slate-800 group-hover:text-slate-900 transition">
						{{ link.title }}
					</div>
				</div>
				<div class="w-7 h-7 rounded-full flex items-center justify-center text-slate-400 group-hover:text-slate-700 group-hover:bg-slate-100 transition">
					<FeatherIcon name="chevron-right" class="h-4 w-4" />
				</div>
			</router-link>
		</div>
	</div>
</template>

<script setup>
import { FeatherIcon } from "frappe-ui"

const props = defineProps({
	title: {
		type: String,
		required: false,
		default: "",
	},
	items: {
		type: Array,
		required: true,
	},
})

function getIconBadgeClass(title, idx) {
	const t = (title || "").toLowerCase()
	if (t.includes("attendance")) return "bg-blue-50 text-blue-600"
	if (t.includes("shift")) return "bg-purple-50 text-purple-600"
	if (t.includes("leave")) return "bg-amber-50 text-amber-600"
	if (t.includes("expense") || t.includes("claim")) return "bg-emerald-50 text-emerald-600"
	if (t.includes("advance")) return "bg-teal-50 text-teal-600"
	if (t.includes("salary") || t.includes("slip")) return "bg-indigo-50 text-indigo-600"

	const fallbacks = [
		"bg-blue-50 text-blue-600",
		"bg-purple-50 text-purple-600",
		"bg-amber-50 text-amber-600",
		"bg-emerald-50 text-emerald-600",
		"bg-teal-50 text-teal-600",
		"bg-indigo-50 text-indigo-600",
	]
	return fallbacks[idx % fallbacks.length]
}
</script>
